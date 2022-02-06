# Winter ABC Mentoring Program

Team 8 Mentor Hyunjoon Jeong

## Class 08 Security & Cryptography - Activity
In this acitivity, students will hook "printf" system call in Ubuntu.

### How to run?
~~~
gcc -o hooker.so hooker.c -shared -fPIC -ldl
gcc c_test.c
export LD_PRELOAD=./hooker.so
./a.out
~~~
