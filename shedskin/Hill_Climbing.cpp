#include "builtin.hpp"
#include "random.hpp"
#include "time.hpp"
#include "math.hpp"
#include "Hill_Climbing.hpp"
#include "Basic.hpp"

namespace __Hill_Climbing__ {


str *__name__;



/**
class Individual
*/

class_ *cl_Individual;

list<__ss_int> *Individual::getArr() {
    
    return this->arr;
}

double Individual::getFitness() {
    
    return this->fitness;
}

void *Individual::__init__(list<__ss_int> *arr, double fitness) {
    
    this->arr = arr;
    this->fitness = fitness;
    return NULL;
}

Individual *Initial(list<__ss_int> *arr) {
    double curr_fitness;
    Individual *individual;

    curr_fitness = __Basic__::Fitness(arr);
    individual = (new Individual(arr, curr_fitness));
    return individual;
}

Individual *HC(Individual *individual) {
    double curr_fitness, next_fitness;
    list<__ss_int> *arr;

    arr = individual->getArr();
    curr_fitness = individual->getFitness();
    arr = __Basic__::BitChange(arr);
    next_fitness = __Basic__::Fitness(arr);
    if ((next_fitness>curr_fitness)) {
        curr_fitness = next_fitness;
    }
    individual = (new Individual(arr, curr_fitness));
    return individual;
}

void __init() {
    __name__ = new str("Hill_Climbing");

    cl_Individual = new class_("Individual");
}

} // module namespace

/* extension module glue */

extern "C" {
#include <Python.h>
#include "random.hpp"
#include "time.hpp"
#include "math.hpp"
#include "Hill_Climbing.hpp"
#include "Basic.hpp"
#include <structmember.h>
#include "random.hpp"
#include "time.hpp"
#include "math.hpp"
#include "Hill_Climbing.hpp"
#include "Basic.hpp"

PyObject *__ss_mod_Hill_Climbing;

namespace __Hill_Climbing__ { /* XXX */

/* class Individual */

typedef struct {
    PyObject_HEAD
    __Hill_Climbing__::Individual *__ss_object;
} __ss_Hill_Climbing_IndividualObject;

static PyMemberDef __ss_Hill_Climbing_IndividualMembers[] = {
    {NULL}
};

PyObject *__ss_Hill_Climbing_Individual_getArr(PyObject *self, PyObject *args, PyObject *kwargs) {
    try {

        return __to_py(((__ss_Hill_Climbing_IndividualObject *)self)->__ss_object->getArr());

    } catch (Exception *e) {
        PyErr_SetString(__to_py(e), ((e->message)?(e->message->unit.c_str()):""));
        return 0;
    }
}

PyObject *__ss_Hill_Climbing_Individual_getFitness(PyObject *self, PyObject *args, PyObject *kwargs) {
    try {

        return __to_py(((__ss_Hill_Climbing_IndividualObject *)self)->__ss_object->getFitness());

    } catch (Exception *e) {
        PyErr_SetString(__to_py(e), ((e->message)?(e->message->unit.c_str()):""));
        return 0;
    }
}

PyObject *__ss_Hill_Climbing_Individual___init__(PyObject *self, PyObject *args, PyObject *kwargs) {
    try {
        list<__ss_int> *arg_0 = __ss_arg<list<__ss_int> *>("arr", 0, 0, 0, args, kwargs);
        double arg_1 = __ss_arg<double >("fitness", 1, 0, 0, args, kwargs);

        return __to_py(((__ss_Hill_Climbing_IndividualObject *)self)->__ss_object->__init__(arg_0, arg_1));

    } catch (Exception *e) {
        PyErr_SetString(__to_py(e), ((e->message)?(e->message->unit.c_str()):""));
        return 0;
    }
}

static PyNumberMethods __ss_Hill_Climbing_Individual_as_number = {
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
};

PyObject *__ss_Hill_Climbing_Individual__reduce__(PyObject *self, PyObject *args, PyObject *kwargs);
PyObject *__ss_Hill_Climbing_Individual__setstate__(PyObject *self, PyObject *args, PyObject *kwargs);

static PyMethodDef __ss_Hill_Climbing_IndividualMethods[] = {
    {(char *)"__reduce__", (PyCFunction)__ss_Hill_Climbing_Individual__reduce__, METH_VARARGS | METH_KEYWORDS, (char *)""},
    {(char *)"__setstate__", (PyCFunction)__ss_Hill_Climbing_Individual__setstate__, METH_VARARGS | METH_KEYWORDS, (char *)""},
    {(char *)"getArr", (PyCFunction)__ss_Hill_Climbing_Individual_getArr, METH_VARARGS | METH_KEYWORDS, (char *)""},
    {(char *)"getFitness", (PyCFunction)__ss_Hill_Climbing_Individual_getFitness, METH_VARARGS | METH_KEYWORDS, (char *)""},
    {(char *)"__init__", (PyCFunction)__ss_Hill_Climbing_Individual___init__, METH_VARARGS | METH_KEYWORDS, (char *)""},
    {NULL}
};

int __ss_Hill_Climbing_Individual___tpinit__(PyObject *self, PyObject *args, PyObject *kwargs) {
    if(!__ss_Hill_Climbing_Individual___init__(self, args, kwargs))
        return -1;
    return 0;
}

PyObject *__ss_Hill_Climbing_IndividualNew(PyTypeObject *type, PyObject *args, PyObject *kwargs) {
    __ss_Hill_Climbing_IndividualObject *self = (__ss_Hill_Climbing_IndividualObject *)type->tp_alloc(type, 0);
    self->__ss_object = new __Hill_Climbing__::Individual();
    self->__ss_object->__class__ = __Hill_Climbing__::cl_Individual;
    __ss_proxy->__setitem__(self->__ss_object, self);
    return (PyObject *)self;
}

void __ss_Hill_Climbing_IndividualDealloc(__ss_Hill_Climbing_IndividualObject *self) {
    self->ob_type->tp_free((PyObject *)self);
    __ss_proxy->__delitem__(self->__ss_object);
}

PyObject *__ss_get___ss_Hill_Climbing_Individual_arr(__ss_Hill_Climbing_IndividualObject *self, void *closure) {
    return __to_py(self->__ss_object->arr);
}

int __ss_set___ss_Hill_Climbing_Individual_arr(__ss_Hill_Climbing_IndividualObject *self, PyObject *value, void *closure) {
    try {
        self->__ss_object->arr = __to_ss<list<__ss_int> *>(value);
    } catch (Exception *e) {
        PyErr_SetString(__to_py(e), ((e->message)?(e->message->unit.c_str()):""));
        return -1;
    }
    return 0;
}

PyObject *__ss_get___ss_Hill_Climbing_Individual_fitness(__ss_Hill_Climbing_IndividualObject *self, void *closure) {
    return __to_py(self->__ss_object->fitness);
}

int __ss_set___ss_Hill_Climbing_Individual_fitness(__ss_Hill_Climbing_IndividualObject *self, PyObject *value, void *closure) {
    try {
        self->__ss_object->fitness = __to_ss<double >(value);
    } catch (Exception *e) {
        PyErr_SetString(__to_py(e), ((e->message)?(e->message->unit.c_str()):""));
        return -1;
    }
    return 0;
}

PyGetSetDef __ss_Hill_Climbing_IndividualGetSet[] = {
    {(char *)"arr", (getter)__ss_get___ss_Hill_Climbing_Individual_arr, (setter)__ss_set___ss_Hill_Climbing_Individual_arr, (char *)"", NULL},
    {(char *)"fitness", (getter)__ss_get___ss_Hill_Climbing_Individual_fitness, (setter)__ss_set___ss_Hill_Climbing_Individual_fitness, (char *)"", NULL},
    {NULL}
};

PyTypeObject __ss_Hill_Climbing_IndividualObjectType = {
    PyObject_HEAD_INIT(NULL)
    0,              /* ob_size           */
    "Hill_Climbing.Individual",        /* tp_name           */
    sizeof(__ss_Hill_Climbing_IndividualObject), /* tp_basicsize      */
    0,              /* tp_itemsize       */
    (destructor)__ss_Hill_Climbing_IndividualDealloc, /* tp_dealloc        */
    0,              /* tp_print          */
    0,              /* tp_getattr        */
    0,              /* tp_setattr        */
    0,              /* tp_compare        */
    0,              /* tp_repr           */
    &__ss_Hill_Climbing_Individual_as_number,  /* tp_as_number      */
    0,              /* tp_as_sequence    */
    0,              /* tp_as_mapping     */
    0,              /* tp_hash           */
    0,              /* tp_call           */
    0,              /* tp_str            */
    0,              /* tp_getattro       */
    0,              /* tp_setattro       */
    0,              /* tp_as_buffer      */
    Py_TPFLAGS_DEFAULT, /* tp_flags          */
    0,              /* tp_doc            */
    0,              /* tp_traverse       */
    0,              /* tp_clear          */
    0,              /* tp_richcompare    */
    0,              /* tp_weaklistoffset */
    0,              /* tp_iter           */
    0,              /* tp_iternext       */
    __ss_Hill_Climbing_IndividualMethods,      /* tp_methods        */
    __ss_Hill_Climbing_IndividualMembers,      /* tp_members        */
    __ss_Hill_Climbing_IndividualGetSet,       /* tp_getset         */
    0,              /* tp_base           */
    0,              /* tp_dict           */
    0,              /* tp_descr_get      */
    0,              /* tp_descr_set      */
    0,              /* tp_dictoffset     */
    __ss_Hill_Climbing_Individual___tpinit__, /* tp_init           */
    0,              /* tp_alloc          */
    __ss_Hill_Climbing_IndividualNew,          /* tp_new            */
};

PyObject *__ss_Hill_Climbing_Individual__reduce__(PyObject *self, PyObject *args, PyObject *kwargs) {
    PyObject *t = PyTuple_New(3);
    PyTuple_SetItem(t, 0, PyObject_GetAttrString(__ss_mod_Hill_Climbing, "__newobj__"));
    PyObject *a = PyTuple_New(1);
    PyTuple_SetItem(a, 0, (PyObject *)&__ss_Hill_Climbing_IndividualObjectType);
    PyTuple_SetItem(t, 1, a);
    PyObject *b = PyTuple_New(2);
    PyTuple_SetItem(b, 0, __to_py(((__ss_Hill_Climbing_IndividualObject *)self)->__ss_object->arr));
    PyTuple_SetItem(b, 1, __to_py(((__ss_Hill_Climbing_IndividualObject *)self)->__ss_object->fitness));
    PyTuple_SetItem(t, 2, b);
    return t;
}

PyObject *__ss_Hill_Climbing_Individual__setstate__(PyObject *self, PyObject *args, PyObject *kwargs) {
    int l = PyTuple_Size(args);
    PyObject *state = PyTuple_GetItem(args, 0);
    ((__ss_Hill_Climbing_IndividualObject *)self)->__ss_object->arr = __to_ss<list<__ss_int> *>(PyTuple_GetItem(state, 0));
    ((__ss_Hill_Climbing_IndividualObject *)self)->__ss_object->fitness = __to_ss<double >(PyTuple_GetItem(state, 1));
    return Py_None;
}

} // namespace __Hill_Climbing__

namespace __Hill_Climbing__ { /* XXX */
PyObject *Global_Hill_Climbing_HC(PyObject *self, PyObject *args, PyObject *kwargs) {
    try {
        Individual *arg_0 = __ss_arg<Individual *>("individual", 0, 0, 0, args, kwargs);

        return __to_py(__Hill_Climbing__::HC(arg_0));

    } catch (Exception *e) {
        PyErr_SetString(__to_py(e), ((e->message)?(e->message->unit.c_str()):""));
        return 0;
    }
}

PyObject *Global_Hill_Climbing_Initial(PyObject *self, PyObject *args, PyObject *kwargs) {
    try {
        list<__ss_int> *arg_0 = __ss_arg<list<__ss_int> *>("arr", 0, 0, 0, args, kwargs);

        return __to_py(__Hill_Climbing__::Initial(arg_0));

    } catch (Exception *e) {
        PyErr_SetString(__to_py(e), ((e->message)?(e->message->unit.c_str()):""));
        return 0;
    }
}

static PyNumberMethods Global_Hill_Climbing_as_number = {
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
};

static PyMethodDef Global_Hill_ClimbingMethods[] = {
    {(char *)"__newobj__", (PyCFunction)__ss__newobj__, METH_VARARGS | METH_KEYWORDS, (char *)""},
    {(char *)"HC", (PyCFunction)Global_Hill_Climbing_HC, METH_VARARGS | METH_KEYWORDS, (char *)""},
    {(char *)"Initial", (PyCFunction)Global_Hill_Climbing_Initial, METH_VARARGS | METH_KEYWORDS, (char *)""},
    {NULL}
};

PyMODINIT_FUNC initHill_Climbing(void) {

    __ss_mod_Hill_Climbing = Py_InitModule((char *)"Hill_Climbing", Global_Hill_ClimbingMethods);
    if(!__ss_mod_Hill_Climbing)
        return;

    if (PyType_Ready(&__ss_Hill_Climbing_IndividualObjectType) < 0)
        return;

    PyModule_AddObject(__ss_mod_Hill_Climbing, "Individual", (PyObject *)&__ss_Hill_Climbing_IndividualObjectType);


}

PyMODINIT_FUNC addHill_Climbing(void) {

}

} // namespace __Hill_Climbing__

} // extern "C"
namespace __Hill_Climbing__ { /* XXX */

PyObject *Individual::__to_py__() {
    PyObject *p;
    if(__ss_proxy->has_key(this))
        p = (PyObject *)(__ss_proxy->__getitem__(this));
    else {
        __ss_Hill_Climbing_IndividualObject *self = (__ss_Hill_Climbing_IndividualObject *)(__ss_Hill_Climbing_IndividualObjectType.tp_alloc(&__ss_Hill_Climbing_IndividualObjectType, 0));
        self->__ss_object = this;
        __ss_proxy->__setitem__(self->__ss_object, self);
        p = (PyObject *)self;
    }
    Py_INCREF(p);
    return p;
}

} // module namespace

namespace __shedskin__ { /* XXX */

template<> __Hill_Climbing__::Individual *__to_ss(PyObject *p) {
    if(p == Py_None) return NULL;
    if(PyObject_IsInstance(p, (PyObject *)&__Hill_Climbing__::__ss_Hill_Climbing_IndividualObjectType)!=1)
        throw new TypeError(new str("error in conversion to Shed Skin (Individual expected)"));
    return ((__Hill_Climbing__::__ss_Hill_Climbing_IndividualObject *)p)->__ss_object;
}
}
