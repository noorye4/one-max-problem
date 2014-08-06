#ifndef __BASIC_HPP
#define __BASIC_HPP

using namespace __shedskin__;
namespace __Basic__ {



extern str *__name__;


void __init();
list<__ss_int> *Gen_RandArr(__ss_int size);
double Fitness(list<__ss_int> *arr);
list<__ss_int> *BitChange(list<__ss_int> *arr);

extern "C" {
PyMODINIT_FUNC initBasic(void);

PyMODINIT_FUNC addBasic(void);

}
} // module namespace
namespace __shedskin__ { /* XXX */

}
#endif
