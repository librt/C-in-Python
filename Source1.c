#include <stdlib.h>
#ifdef __cplusplus
extern "C" {
#endif

	__declspec(dllexport) int dot(int *a, int *b, size_t length) {
	int result = 0;
	while (length--> 0) {
		result += a[length] * b[length];
	}
	return result;
}

#ifdef __cplusplus
}
#endif