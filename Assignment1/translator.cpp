#include<iostream>
#include<fstream>
#include<string>

using namespace std;

int main(int argc, char *argv[])
{
    ifstream f1(argv[1]);
    ofstream f2(argv[2]);

    string line;

    f2 << "BITS 64" << endl << endl;

    while( getline(f1, line) )
    {
        string tmp = line;

        int pos = line.find("mov eax, 1");
        if( pos != string::npos )
            tmp.replace(pos, 11, "mov rax, 60");

        pos = line.find("mov ebx, 0");
        if( pos != string::npos )
            tmp.replace(pos, 10, "mov rdi, 0");

        pos = line.find("int 80h");
        if( pos != string::npos )
            tmp.replace(pos, 7, "syscall");

        pos = line.find("ecx");
        if( pos != string::npos )
            tmp.replace(pos, 3, "rcx");

        pos = line.find("edx");
        if( pos != string::npos )
            tmp.replace(pos, 3, "rdx");

        f2 << tmp << endl;
    }
    return 0;
}
