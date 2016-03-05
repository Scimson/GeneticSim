#lang racket

(define mutation-probablilty 0.05)

(define mutation-size 0.1)

(define random-dna-range 20)

(define generation-size 8)

;; A Segment is a Number

;; A DNA-Strand is a (listof Segments)

;; A DNA is a DNA-Strand DNA-Strand
(struct DNA (strand1 strand2) #:transparent)

;; reproduce: DNA DNA -> DNA
(define (reproduce dna1 dna2)
  (DNA (mutate (select-segments dna1))
       (mutate (select-segments dna2))))

;; mutate: DNA-Strand -> DNA-Strand
(define (mutate strand)
  (map (λ (x) (cond [(< (random) mutation-probablilty) (* (+ 1 (* (- (random) 0.5) mutation-size) ) x)]
                    [else x]))
       strand))


;; select-segments: GenePair -> Gene
(define (select-segments dna)
  (map (λ (x1 x2) (if (< (random) 0.5) x1 x2))
       (DNA-strand1 dna)
       (DNA-strand2 dna)))

(define (build-dna num) (DNA (build-list 10 (λ (x) num))
                             (build-list 10 (λ (x) num))))

(define (random-dna) (DNA (build-list 3 (λ (x) (* random-dna-range (- (random) 0.5))))
                          (build-list 3 (λ (x) (* random-dna-range (- (random) 0.5))))))

(define (random-generation size) (build-list size (λ(x)(random-dna))))

(define (dna-to-n-args n dna) (map (λ (x1 x2) (/ (+ x1 x2) 2))
                                   (take (DNA-strand1 dna) n)
                                   (take (DNA-strand2 dna) n)))






(define test-gen (list
                  (DNA '(-6.641440121787494 9.391572762617642 -2.6246627946220933) '(-7.114217965807146 1.1256782929741527 -8.354882616041131))
                  (DNA '(-9.684298577330566 2.533795630333362 1.1298079497646674) '(-9.650180807159657 5.067004727650664 -7.626759681470229))
                  (DNA '(0.40781875718997496 -9.402621215150042 3.293569000685206) '(-6.878973113099674 -8.082556487333903 -6.2038947945484235))
                  (DNA '(0.5604159032382339 7.880232161630014 -0.317807734502481) '(-7.612795197279518 -2.475480212573866 -6.586427462747533))))


;; A Generation is a (listof DNA)

(define (display-strand strand) (display (map (λ (x) (~r x #:precision '(= 3) #:min-width 6 #:pad-string "0" #:sign '++)) strand)))

(define (display-dna dna)
  (display "DNA")
  (display " ")
  (display-strand (DNA-strand1 dna))
  (display " ")
  (display-strand (DNA-strand2 dna)))

(define (gen->scored-gen gen) (map (λ (dna) (list (apply function-to-maximize (dna-to-n-args 3 dna)) dna)) gen))

(define (display-scored-gen scored-gen)
  (for-each (λ (scored-dna)
              (let ([score (first scored-dna)]
                    [dna (second scored-dna)])
                (display (~r score #:precision '(= 3) #:min-width 7 #:pad-string "0" #:sign '++))
                (display " ")
                (display-dna dna)
                (newline)))
            scored-gen))


(define (next-generation scored-generation)
  (let ([top1 (second (first scored-generation))]
        [top2 (second (second scored-generation))])
    (build-list generation-size (λ(_)(reproduce top1 top2)))))

(define (run-n-generations n num-gens gen)
  (cond [(>= 0 n) (display "MASS EXTINCTION")]
        [else
         (let ([scored-gen (sort (gen->scored-gen gen) > #:key first)])
           (display "GENERATION: ")
           (display (- num-gens n))
           (newline)
           (display-scored-gen scored-gen)
           (display "-----------------")
           (newline)
           (run-n-generations (sub1 n) num-gens (next-generation scored-gen)))]))

(define (function-to-maximize x1 x2 x3) (+ (* 3 x1) (- x2) (* x3 x3)))

(define (run n) (run-n-generations n n (random-generation generation-size)))