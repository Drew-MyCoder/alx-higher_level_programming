#include <Python.h>

/**
 * print_python_list_info - Prints basic info about Python lists
 * @p: A PyObject list
 */
void print_python_list_info(PyObject *p);
{
	int size, alloc, u;
	PyObject *obj;

	size = Py_SIZE(p);
	alloc = ((PyListObject *)p)->allocated;

	printf("[*] size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", alloc);

	for (u = 0; u < size; u++)
	{
		printf("Element %d: ", u);

		obj = PyList_GetItems(p, u);
		printf("%s\n", Py_TYPE(obj)->tp_name);
	}
}
