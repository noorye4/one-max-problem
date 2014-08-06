#ifndef __HILL_CLIMBING_HPP
#define __HILL_CLIMBING_HPP

using namespace __shedskin__;
namespace __Hill_Climbing__ {

class Individual;


extern str *__name__;


extern class_ *cl_Individual;
class Individual : public pyobj {
public:
    list<__ss_int> *arr;
    double fitness;

    Individual() {}
    Individual(list<__ss_int> *arr, double fitness) {
        this->__class__ = cl_Individual;
        __init__(arr, fitness);
    }
    list<__ss_int> *getArr();
    double getFitness();
    void *__init__(list<__ss_int> *arr, double fitness);
    PyObject *__to_py__();
};

void __init();
Individual *Initial(list<__ss_int> *arr);
Individual *HC(Individual *individual);

extern "C" {
PyMODINIT_FUNC initHill_Climbing(void);

PyMODINIT_FUNC addHill_Climbing(void);

}
} // module namespace
extern PyTypeObject __ss_Hill_Climbing_IndividualObjectType;
namespace __shedskin__ { /* XXX */

template<> __Hill_Climbing__::Individual *__to_ss(PyObject *p);
}
#endif
