#ifndef __HC_TEST_HPP
#define __HC_TEST_HPP

using namespace __shedskin__;

namespace __Hill_Climbing__ { /* XXX */
class Individual;
}
namespace __hc_test__ {

extern str *const_0, *const_1, *const_2;



extern __ss_int timezone;
extern tuple2<str *, str *> *tzname;
extern str *__name__;
extern list<__ss_int> *arr;


void *exp_HC(list<__ss_int> *arr, __ss_int times);

extern "C" {
PyMODINIT_FUNC inithc_test(void);

PyMODINIT_FUNC addhc_test(void);

}
} // module namespace
namespace __shedskin__ { /* XXX */

}
#endif
