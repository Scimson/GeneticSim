#include "Gene.h"



Gene::Gene() {}

Gene::Gene(Gene &g) {

}


Gene::~Gene() {}

// TODO: Add random mutations
Gene &Gene::newDuplicate() {
    return *new Gene(*this);
}