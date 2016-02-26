#pragma once
class Gene {
public:
    Gene();
    Gene(Gene &g);
    virtual ~Gene();
    Gene &newDuplicate();

};

