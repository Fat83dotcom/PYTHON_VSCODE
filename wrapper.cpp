#include <stdio.h>
#include <Python.h>
#include <readline/readline.h>
#include <readline/history.h>

PyObject*

fn_readline(PyObject *self, PyObject *args) {
  char *prompt;
  char *line;
  PyObject *o;

  if (!PyArg_ParseTuple(args, "s", &prompt)) {
      return NULL;
  }

  line = readline(prompt);

  o = Py_BuildValue("s", line);
  free(line);

  return o;
}
PyObject *
fn_add_history(PyObject *self, PyObject *args)
{
  char *line;
  int status;
  PyObject *o;

  if (!PyArg_ParseTuple(args, "s", &line))
    NULL;

  status = add_history(line);

  o = Py_BuildValue("i", status);
  return o;
}
static PyMethodDef
methods[] = {
  {"readline", fn_readline, METH_VARARGS, NULL},
  {"add_history", fn_add_history, METH_VARARGS, NULL},
  {NULL, NULL, 0, NULL}
};

PyMODINIT_FUNC
initreadline(void)
{
  (void) Py_InitModule("readline", methods);
}