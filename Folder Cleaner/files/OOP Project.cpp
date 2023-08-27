#include<iostream>
#include<fstream>
#include<conio.h>
#include<windows.h>
#include<String>

using namespace std;


class Student {
protected:

	string name;
	string Email;
	string Gender;
	string phone;
	int marks;

public:

	Student() {
		name = "";
		Email = "";
		Gender = "";
		phone = "";
		marks = 0;
	}

};
class Form : public Student {
public:
	void insert() {

		system("cls");
		cout << "\t\t\t-------------------------------------------" << endl;
		cout << "\t\t\t--------Welcome to Admission Form----------" << endl;
		cout << "\t\t\t-------------------------------------------" << endl;
		cout << "\t\t\tEnter Your Name :";
		cin >> name;
		cout << "\t\t\tEnter Your Gender : ";
		cin >> Gender;
		cout << "\t\t\tEnter Your Email :";
		cin >> Email;
		cout << "\t\t\tEnter Your phone :";
		cin >> phone;
		cout << "\t\t\tEnter Your Marks :";
		cin >> marks;


		ofstream myfile;
		myfile.open("StudentRecord.txt", ios::app);
		myfile << "\n name : " << name;
		myfile << "\n Gender : " << Gender;
		myfile << "\n Email :" << Email;
		myfile << "\n Phone :" << phone;
		myfile << "\n Marks :" << marks << "\n";

		myfile.close();


		char E = 0;
		cout << "\n\t\tPress Y to Go Back = ";
		cin >> E;
		if (E == 'y' || E == 'Y') {
			menu();
		}

	}


	void menu() {

		int choice;
		system("cls");

		cout << "\t\t\t-------------------------------------------" << endl;
		cout << "\t\t\t-----Welcome to Admission Admin portal-----" << endl;
		cout << "\t\t\t-------------------------------------------" << endl;
		cout << "\n\t\t\t 1.Enter to Fill the Form " << endl;
		cout << "\n\t\t\t 2.Enter To Select Your Cousre " << endl;
		cout << "\n\t\t\t 3.Enter To print Your Chalan " << endl;
		cout << "\n\t\t\t 4.Enter Admin Mode " << endl;
		cout << "\n\t\t\t 5.Exit " << endl;

	Again:


		cout << "\n\t\t\tEnter Your choice :";
		cin >> choice;
		switch (choice) {
		case 1:
			insert();
			break;



		case 4:
			admin();
			break;
		case 5:
			exit(0);

		default:
			//setcolor(0x0C);
			cout << "\n\t\t\t Inavalid Number .. Try Again " << endl;
			//setcolor(0x07);
			goto Again;
			break;




		}
	}
	void admin() {

		system("cls");

		cout << "\t\t\t-------------------------------------------" << endl;
		cout << "\t\t\t-----Welcome To  Admin portal-----" << endl;
		cout << "\t\t\t-------------------------------------------" << endl;
		cout << "\n\t\t\t 1.Enter To Show Data Of Student " << endl;
		cout << "\n\t\t\t 2.Enter to Modify Record " << endl;
		cout << "\n\t\t\t 3.Enter to Delete Record " << endl;
		cout << "\n\t\t\t 4.Enter To Back Main Menu " << endl;

	Again:
		int choice;
		cout << "\n\t\t\tEnter Your choice ";
		cin >> choice;
		switch (choice) {
		case 1:
			showData();
			break;
		case 4:
			menu();
			break;
		case 5:
			exit(0);

		default:
			cout << "\n\t\t\t Inavalid Number .. Try Again " << endl;
			goto Again;

		}

	}

	void showData() {
		system("cls");


		string line;
		ifstream file;
		file.open("StudentRecord.txt");


		if (file.is_open())
		{

			while (getline(file, line))
			{

				cout << line << endl;

			}
			file.close();


		}






		else {
			cout << "file dosenot open ";
		}


		char E = 0;
		cout << "\n\t\tPress Y to Go Back = ";
		cin >> E;
		if (E == 'y' || E == 'Y') {
			admin();
		}

	}
};



class Pass :public Form {
public:

	void pass() {
		int choice;
		int x = 1234;
		system("cls");

		cout << "\t\t\t---------------------------------------------" << endl;
		cout << "\t\t\t-------Welcome to Admission login form-------" << endl;
		cout << "\t\t\t---------------------------------------------" << endl;

	start:
		cout << "\n\t\t\tENTER PASSWORD TO LOGIN IN =";

		cin >> choice;
		if (choice == x) {
			cout << "\n\t\t\tLogin successfully " << endl;
		}
		else {

			cout << "\n\t\t\tWrong PassWord .Enter Correct Pass " << endl;
			//setcolor(0x07);
			goto start;
		}


		cout << "\n\n\n\n\n";
		cout << "\t\t\t Loading";
		char y = 219;
		for (int a = 0; a < 30; a++) {
			cout << y;
			Sleep(100);

		}


		system("cls");
		menu();
	}



};

int main() {
	Pass s1;
	s1.pass();

}