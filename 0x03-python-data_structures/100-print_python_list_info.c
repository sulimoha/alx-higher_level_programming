#include "/usr/include/python3.4/pyhon.h"
#include "/usr/include/python3.4/listobject.h"
#include "/usr/include/python3.4/object.h"
#include <stdio.h>

void print_python_list_info(PyObject *p)
{
	int i = 0;
	int len_list = 0;
	pyobject *element;
	pylistObject *clone = (pyListObject *) p;
	
	len_list = py_SIZE(p);
	printf("[*] size of the python List = %d\n", len_list);
	printf("[*] Allocated = %d\n", (int) clone->allocated);
	for (; i< len_list; ++i)
	{
		element = pyList_GET_ITEM(p, i);
		printf("Element %d: %s\n", i, item->ob_type->tp_name);
	}
	return;
}
