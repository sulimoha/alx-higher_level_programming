#include "python.h"

#include <stdio.h>

void print_python_list_info(PyObject *p)
{
	Py_ssize_t i = 0;
	Py_ssize_t len_list;
	PyObject *element;
	PyListObject *clone;
	struct_typeobject *type;

	if (strcmp(p->ob_type->tp_name, "clone") == 0)
	{
		clone = (PyListObject *)p;
		len_list = clone->ob_base.ob_size;
		printf("[*] size of the python List = %d\n", len_list);
		printf("[*] Allocated = %d\n", (int) clone->allocated);
		for (; i < len_list; ++i)
		{
			element = clone->ob_item[i];
			type = element->ob_type;
			printf("Element %d: %s\n", i, type->tp_name);
		}
	}
}
