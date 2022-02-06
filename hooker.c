#define _GNU_SOURCE
#include <stdio.h>
#include <dlfcn.h>

int (*printf_real)(const char *, ...) = NULL;

void __attribute__((constructor)) init_hooking() {

  printf_real = dlsym(RTLD_NEXT, "printf");
  fprintf(stderr, "real printf address: %p\n", printf_real);
}


int printf(const char *format, ...) {

  return printf_real("Your message was hooked!");
}
