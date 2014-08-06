#include "builtin.hpp"
#include "math.hpp"
#include "random.hpp"
#include "time.hpp"
#include "Basic.hpp"

namespace __Basic__ {


str *__name__;



list<__ss_int> *Gen_RandArr(__ss_int size) {
    list<__ss_int> *arr;
    __ss_int __0, __1, i, x;

    arr = (new list<__ss_int>());

    FAST_FOR(i,0,size,1,0,1)
        x = __random__::randint(0, 1);
        arr->append(x);
    END_FOR

    return arr;
}

double Fitness(list<__ss_int> *arr) {
    __iter<__ss_int> *__3;
    double counter, fitness;
    __ss_int __4, i;
    list<__ss_int> *__2;
    list<__ss_int>::for_in_loop __5;

    fitness = 0.0;
    counter = 0.0;

    FOR_IN(i,arr,2,4,5)
        counter = (counter+1.0);
        if ((i==0)) {
            fitness = (fitness+1.0);
        }
    END_FOR

    return fitness;
}

list<__ss_int> *BitChange(list<__ss_int> *arr) {
    __ss_int crpt, length;

    length = len(arr);
    crpt = __random__::randint(0, (length-1));
    if ((arr->__getfast__(crpt)==1)) {
        arr->__setitem__(crpt, 0);
    }
    return arr;
}

void __init() {
    __name__ = new str("Basic");

}

} // module namespace

/* extension module glue */

extern "C" {
#include <Python.h>
#include "math.hpp"
#include "random.hpp"
#include "time.hpp"
#include "Basic.hpp"
#include <structmember.h>
#include "math.hpp"
#include "random.hpp"
#include "time.hpp"
#include "Basic.hpp"

PyObject *__ss_mod_Basic;

namespace __Basic__ { /* XXX */
PyObject *Global_Basic_Gen_RandArr(PyObject *self, PyObject *args, PyObject *kwargs) {
    try {
        __ss_int arg_0 = __ss_arg<__ss_int >("size", 0, 0, 0, args, kwargs);

        return __to_py(__Basic__::Gen_RandArr(arg_0));

    } catch (Exception *e) {
        PyErr_SetString(__to_py(e), ((e->message)?(e->message->unit.c_str()):""));
        return 0;
    }
}

PyObject *Global_Basic_BitChange(PyObject *self, PyObject *args, PyObject *kwargs) {
    try {
        list<__ss_int> *arg_0 = __ss_arg<list<__ss_int> *>("arr", 0, 0, 0, args, kwargs);

        return __to_py(__Basic__::BitChange(arg_0));

    } catch (Exception *e) {
        PyErr_SetString(__to_py(e), ((e->message)?(e->message->unit.c_str()):""));
        return 0;
    }
}

PyObject *Global_Basic_Fitness(PyObject *self, PyObject *args, PyObject *kwargs) {
    try {
        list<__ss_int> *arg_0 = __ss_arg<list<__ss_int> *>("arr", 0, 0, 0, args, kwargs);

        return __to_py(__Basic__::Fitness(arg_0));

    } catch (Exception *e) {
        PyErr_SetString(__to_py(e), ((e->message)?(e->message->unit.c_str()):""));
        return 0;
    }
}

static PyNumberMethods Global_Basic_as_number = {
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

static PyMethodDef Global_BasicMethods[] = {
    {(char *)"__newobj__", (PyCFunction)__ss__newobj__, METH_VARARGS | METH_KEYWORDS, (char *)""},
    {(char *)"Gen_RandArr", (PyCFunction)Global_Basic_Gen_RandArr, METH_VARARGS | METH_KEYWORDS, (char *)""},
    {(char *)"BitChange", (PyCFunction)Global_Basic_BitChange, METH_VARARGS | METH_KEYWORDS, (char *)""},
    {(char *)"Fitness", (PyCFunction)Global_Basic_Fitness, METH_VARARGS | METH_KEYWORDS, (char *)""},
    {NULL}
};

PyMODINIT_FUNC initBasic(void) {

    __ss_mod_Basic = Py_InitModule((char *)"Basic", Global_BasicMethods);
    if(!__ss_mod_Basic)
        return;



}

PyMODINIT_FUNC addBasic(void) {

}

} // namespace __Basic__

} // extern "C"
