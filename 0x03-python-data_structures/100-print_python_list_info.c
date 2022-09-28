#include "python.h"

#include <stdio.h>

void print_python_list_info(PyObject *p)
{
	int i = 0;
	int len_list = 0;
	PyObject *element;
	PyListObject *clone = (PyListObject *) p;

	len_list = Py_SIZE(p);
	printf("[*] size of the python List = %d\n", len_list);
	printf("[*] Allocated = %d\n", (int) clone->allocated);
	for (; i < len_list; ++i)
	{
		element = PyList_GET_ITEM(p, i);
		printf("Element %d: %s\n", i, item->ob_type->tp_name);
	}
}
