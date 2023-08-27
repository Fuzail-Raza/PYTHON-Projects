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
	int roll_no;
	string Degree;
	int Matric_Marks;
	int Inter_mark;
	int total;

	int Scholarship;
	int total_fee;
	

public:

	Student() {

		name = "";
		Email = "";
		Gender = "";
		phone = "";
		roll_no = 38602;
		Matric_Marks = 0;
		Inter_mark=0;
		total = 0;
		Scholarship = 0;
		total_fee = 0;
		Degree = "";
	}

};
class Form : public Student {
public:
	void insert() {

		system("cls");
		int After_Scholarship;
		
		
		cout << "\t\t\t-------------------------------------------" << endl;
		cout << "\t\t\t--------Welcome to Admission Form----------" << endl;
		cout << "\t\t\t-------------------------------------------" << endl;
		cout << "\t\t\tEnter Your Name :";
		cin >> name;
		cout << "\t\t\tEnter Your Gender : ";
		cin >> Gender;
	//	cout << "\t\t\tEnter Roll Number :";
	//	cin >> roll_no;
		cout << "\t\t\tEnter Your Email :";
		cin >> Email;
		cout << "\t\t\tEnter Your phone :";
		cin >> phone;
	//	cout << "\t\t\tEnter Your Marks :";
		//cin >> marks;

		

		system("cls");

		int choice;
		cout << "\n------------------------------------------------------------------------------------------------------------";
		cout << "\n------------------------------------- Students Courses -----------------------------------------------------" << endl;
		


		cout << "\n\t\t\tEnter Your Course Which Do you want To Study------" << endl;
		cout << "\n\t\t\t (1) For  BS Computer Science  Press  1 ---" << endl;
		cout << "\n\t\t\t (2) For  BS Software Engeneering press 2 ----" << endl;
		cout << "\n\t\t\t (3) For  BS Physics press 3 -----" << endl;

		cout << "\n\t\t\tEnter Your Choice : ";
		cin >> choice;

	
		switch (choice)
		{
		case 1:

			system("cls");
			 Degree = "BSCS";
			 total_fee = 87100;
			
			
			cout << "\n\t\t\tYou are Applying For BS in Computer Science " << endl;

			cout << "\n\t\t\tEnter Your Marks of Matric : ";
			cin >> Matric_Marks;
			cout << "\n\t\t\tEnter Your Marks of Intermediate : ";
			cin >>Inter_mark;
			if (Inter_mark <= 900) {
			///	cout << "\n\t\t\tYou have got Super Section " << endl;
				Scholarship = 75;
				After_Scholarship = total_fee - (total_fee * Scholarship / 100);

				cout << "\n\t\t\tYou have got 75 % Scholarship :";
				cout << "\n\t\t\tYour Total Fesss of BS Computer Science is : " << total_fee;
				cout << "\n\t\t\tYour fess after Scholarship is : " << After_Scholarship;
				


			}
			else if (Inter_mark >= 900|| Inter_mark <=1100) {
			////	cout << "\n\t\t\tYou have got Super Section " << endl;
				Scholarship = 100;
				After_Scholarship = total_fee - (total_fee * Scholarship / 100);

				cout << "\n\t\t\tYou have got 100% Scholarship :";
				cout << "\n\t\t\tYour Total Fesss Of BS Computer Science is : " << total_fee;
				cout << "\n\t\t\tYour fess after Scholarship is : " << After_Scholarship;
			
			}
			else if (Inter_mark < 900 || Inter_mark >= 700) {
				//// cout << "\n\t\t\tYou have got Model Section ";

				Scholarship = 50;
				After_Scholarship = total_fee - (total_fee * Scholarship / 100);
				cout << "\n\t\t\tYour Total Fesss of BS Compter Science is : " << total_fee;
				cout << "\n\t\t\tYour fess after Discount is : " << After_Scholarship;
				
			}
			else if (Matric_Marks < 700) {
				cout << "\n\t\t\tYou are not Eligible for Scholarship ";

				cout << "Your Fess is " << total_fee;
			}

			
			break;

		case 2:

			system("cls");
			 total_fee = 150000;
			 Degree = "Fsc Engineering";


			cout << "\n\t\t\tAs You have Seletcted The FSC ( Fsc engineering) Subject " << endl;

			cout << "\n\t\t\tEnter Your Marks of Matric : ";
			cin >> Matric_Marks;

			if (Matric_Marks <= 900) {
				cout << "\n\t\t\tYou have got Super Section " << endl;
				Scholarship = 65;
				After_Scholarship = total_fee - (total_fee * Scholarship / 100);

				cout << "\n\t\t\tYou have got 75 Discount :";
				cout << "\n\t\t\tYour Total Fesss is : " << total_fee;
				cout << "\n\t\t\tYour fess after Discount is : " << After_Scholarship;
				


			}
			else if (Matric_Marks >= 900 || Matric_Marks <= 1100) {
				cout << "\n\t\t\tYou have got Super Section " << endl;
				Scholarship = 85;
				After_Scholarship = total_fee - (total_fee * Scholarship / 100);

				cout << "\n\t\t\tYou have got 95 Discount :";
				cout << "\n\t\t\tYour Total Fesss is : " << total_fee;
				cout << "\n\t\t\tYour fess after Discount is : " << After_Scholarship;
			}
			else if (Matric_Marks < 900 || Matric_Marks >= 700) {
				cout << "\n\t\t\tYou have got Model Section ";

				Scholarship = 50;
				int After_discount = total_fee - (total_fee * Scholarship / 100);

				cout << "\n\t\t\tYour Total Fesss is : " << total_fee;
				cout << "\n\t\t\tYour fess after Discount is : " << After_discount;
				
			}
			else if (Matric_Marks < 700) {
				cout << "\n\t\t\tYou dont get any Section ";

				cout << "Your Fess is " << total_fee;
			}


			break;


		case 3:

			system("cls");
			total_fee = 165000;
			Degree = "Fsc Engineering";


			cout << "\n\t\t\tAs You have Seletcted The FSC ( Fsc Pre Medical's) Subject " << endl;

			cout << "\n\t\t\tEnter Your Marks of Matric : ";
			cin >> Matric_Marks;

			if (Matric_Marks <= 900) {
				cout << "\n\t\t\tYou have got Super Section " << endl;
				Scholarship = 62;
				After_Scholarship = total_fee - (total_fee * Scholarship / 100);

				cout << "\n\t\t\tYou have got 75 Discount :" << endl;
				cout << "\n\t\t\tYour Total Fesss is : " << total_fee << "\n";
				cout << "\n\t\t\tYour fess after Discount is : " << After_Scholarship <<"\n";
				


			}
			else if (Matric_Marks >= 900 || Matric_Marks <= 1100) {
				cout << "\n\t\t\tYou have got Super Section " << endl;
				Scholarship = 88;
				After_Scholarship = total_fee - (total_fee * Scholarship / 100);

				cout << "\n\t\t\tYou have got 95 Discount :" << "\n";
				cout << "\n\t\t\tYour fess after Discount is : " << After_Scholarship << "\n";
				cout << "\n\t\t\tYour Total Fesss is : " << total_fee << "\n";
			}
			else if (Matric_Marks < 900 || Matric_Marks >= 700) {
				cout << "\n\t\t\tYou have got Model Section " << "\n";

				Scholarship = 50;
				int After_discount = total_fee - (total_fee * Scholarship / 100);

				cout << "\n\t\t\tYour fess after Discount is : " << After_discount << "\n";
				cout << "\n\t\t\tYour Total Fesss is : " << total_fee << "\n";
			}
			else if (Matric_Marks < 700) {
				cout << "\n\t\t\tYou dont get any Section " << "\n";

				cout << "Your Fess is " << total_fee << "\n";
			}

			break;
		
		}

		ofstream myfile;
		myfile.open("StudentRecord.txt", ios::app);

		myfile << "\n Student No : " << ++total;
		myfile << "\n name : " << name;
		myfile << "\n Gender : " << Gender;
		myfile << "\n Roll No : " << roll_no--;
		myfile << "\n Email :" << Email;
		myfile << "\n Phone :" << phone;
		myfile << "\n Marks :" << Matric_Marks;
		myfile << "\n Your Subject :" <<Degree;
		myfile << "\n Your Discount: " << After_Scholarship << "\n";

		myfile.close();

		char X;
		cout << "\n\t\tDo You want To add More data? (Y/N)  : ";
		cin >> X;

		if (X == 'n' || X == 'N') {
			cout << "\n\t\tGoing Back To Main Menu " << endl;
			Sleep(1000);
			menu();
		}
		if (X == 'y' || X == 'Y') {
			insert();
		}

	}

	void menu() {

		system("cls");

		cout << "\t\t\t-------------------------------------------" << endl;
		cout << "\t\t\t-----Welcome to Admission Admin portal-----" << endl;
		cout << "\t\t\t-------------------------------------------" << endl;
		cout << "\n\t\t\t 1.Enter to Fill the Form " << endl;
		cout << "\n\t\t\t 2.Enter To print Your Chalan " << endl;
		cout << "\n\t\t\t 3.Enter Admin Mode " << endl;
		cout << "\n\t\t\t 4.Exit " << endl;

		section();
		}


	void section() {
		int choice;
		cout << "\n\t\t\tEnter Your choice :";
		cin >> choice;
		switch (choice) {
		case 1:
			insert();
			break;
		case 2:
			printChalan();
			break;

		case 3:
			admin();
			break;
		case 4:
			exit(0);

		default:
			cout << "\n\t\t\t Inavalid Number .. Try Again " << endl;
			section();
			break;
		}
	}


	void printChalan() {

		string line;
		// For writing text file
		// Creating ofstream & ifstream class object
		ifstream ini_file{
			"StudentRecord.txt"
		}; // This is the original file
		ofstream out_file{ "Chalan.txt" };
		if (ini_file && out_file) {

			while (getline(ini_file, line)) {
				out_file << line << "\n";
			}
			cout << "Copy Finished \n";
		}
		else {
			// Something went wrong
			cout<<"Cannot read File";
		}
		// Closing file
		ini_file.close();
		out_file.close();
		
		system("cls");


		
		ifstream file;
		file.open("Chalan.txt");


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
			menu();
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
		case 2:
			modifyData();
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


	void modifyData() {
		system("cls");


	}
};



class Pass :public Form {
public:

	void password() {
		int choice;
		int x = 1234;
		cout << "\n\n\t\tENTER PASSWORD TO LOGIN IN =";

		cin >> choice;

		if (choice == x) {
			cout << "\n\n\t\tLogin successfully " << endl;
		}
		else {

			cout << "\n\n\t\tWrong PassWord .Enter Correct Pass " << endl;
			password();
		}
	}
	void pass() {
		
		system("cls");

		cout << "\t\t\t\t---------------------------------------------" << endl;
		cout << "\t\t\t\t-------Welcome to University Admission-------" << endl;
		cout << "\t\t\t\t---------------------------------------------" << endl;
		password();
		


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