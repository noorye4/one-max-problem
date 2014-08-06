#include "builtin.hpp"
#include "random.hpp"
#include "math.hpp"
#include "time.hpp"
#include "Hill_Climbing.hpp"
#include "Basic.hpp"
#include "hc_test.hpp"

namespace __hc_test__ {

str *const_0, *const_1, *const_2;

using __time__::time;
using __time__::struct_time;

tuple2<str *, str *> *tzname;
list<__ss_int> *arr;
__ss_int timezone;
str *__name__;



void *exp_HC(list<__ss_int> *arr, __ss_int times) {
    __ss_int __6, __7, i;
    __Hill_Climbing__::Individual *individual;
    double end_time, start_time;
    list<double> *fitness_li;
    file *_file;

    fitness_li = (new list<double>());
    individual = __Hill_Climbing__::Initial(arr);
    _file = open(const_0, const_1);
    start_time = time();

    FAST_FOR(i,0,times,1,6,7)
        individual = __Hill_Climbing__::HC(individual);
        _file->write((repr(individual->getFitness()))->__add__(const_2));
        fitness_li->append(individual->getFitness());
    END_FOR

    _file->close();
    end_time = time();
    print2(NULL,0,1, ___box((end_time-start_time)));
    return NULL;
}

void __init() {
    const_0 = new str("HC_data.txt");
    const_1 = __char_cache[119];;
    const_2 = __char_cache[10];;

    __name__ = new str("hc_test");

    timezone = __time__::timezone;
    tzname = __time__::tzname;
    arr = __Basic__::Gen_RandArr(20);
    exp_HC(arr, 100);
}

} // module namespace

/* extension module glue */

extern "C" {
#include <Python.h>
#include "random.hpp"
#include "math.hpp"
#include "time.hpp"
#include "Hill_Climbing.hpp"
#include "Basic.hpp"
#include "hc_test.hpp"
#include <structmember.h>
#include "random.hpp"
#include "math.hpp"
#include "time.hpp"
#include "Hill_Climbing.hpp"
#include "Basic.hpp"
#include "hc_test.hpp"

PyObject *__ss_mod_hc_test;

namespace __hc_test__ { /* XXX */
PyObject *Global_hc_test_exp_HC(PyObject *self, PyObject *args, PyObject *kwargs) {
    try {
        list<__ss_int> *arg_0 = __ss_arg<list<__ss_int> *>("arr", 0, 0, 0, args, kwargs);
        __ss_int arg_1 = __ss_arg<__ss_int >("times", 1, 0, 0, args, kwargs);

        return __to_py(__hc_test__::exp_HC(arg_0, arg_1));

    } catch (Exception *e) {
        PyErr_SetString(__to_py(e), ((e->message)?(e->message->unit.c_str()):""));
        return 0;
    }
}

static PyNumberMethods Global_hc_test_as_number = {
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

static PyMethodDef Global_hc_testMethods[] = {
    {(char *)"__newobj__", (PyCFunction)__ss__newobj__, METH_VARARGS | METH_KEYWORDS, (char *)""},
    {(char *)"exp_HC", (PyCFunction)Global_hc_test_exp_HC, METH_VARARGS | METH_KEYWORDS, (char *)""},
    {NULL}
};

PyMODINIT_FUNC inithc_test(void) {
    __shedskin__::__init();
    __math__::__init();
    __time__::__init();
    __random__::__init();
    __Basic__::__init();
    __Hill_Climbing__::__init();
    __hc_test__::__init();

    __ss_mod_hc_test = Py_InitModule((char *)"hc_test", Global_hc_testMethods);
    if(!__ss_mod_hc_test)
        return;


    __Hill_Climbing__::initHill_Climbing();
    __Basic__::initBasic();
    __Hill_Climbing__::addHill_Climbing();
    __Basic__::addBasic();
    addhc_test();

}

PyMODINIT_FUNC addhc_test(void) {
    PyModule_AddObject(__ss_mod_hc_test, (char *)"arr", __to_py(__hc_test__::arr));
    PyModule_AddObject(__ss_mod_hc_test, (char *)"timezone", __to_py(__hc_test__::timezone));
    PyModule_AddObject(__ss_mod_hc_test, (char *)"tzname", __to_py(__hc_test__::tzname));

}

} // namespace __hc_test__

} // extern "C"
int main(int, char **) {
    __shedskin__::__init();
    __math__::__init();
    __time__::__init();
    __random__::__init();
    __Basic__::__init();
    __Hill_Climbing__::__init();
    __shedskin__::__start(__hc_test__::__init);
}
