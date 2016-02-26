#pragma once

#include "Gene.h"

class GenePair {
private:
    Gene &m;
    Gene &f;
public:
    GenePair();
    virtual ~GenePair();
    Gene &getOne();
};

