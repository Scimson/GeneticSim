#include "GenePair.h"
#include <stdlib.h>

// Default constructor starts with 2 identical randomized genes
GenePair::GenePair(): m(*new Gene()), f(*new Gene(m)){}


GenePair::~GenePair() {
    delete &m;
    delete &f;
}

Gene &GenePair::getOne() {
    switch (rand() % 2) {
    case 0:
        return m.newDuplicate();
        break;
    case 1:
    default:
        return f.newDuplicate();
        break;
    }
}
