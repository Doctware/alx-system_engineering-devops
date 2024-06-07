My simple web stack diagram -> https://imgur.com/xhtYKYS

in this simple web stack there is a server that host www.foobar.com
and this server was able to connect to with the help of DNS that record 
www.foobar.com pointing to 8.8.8.8 which is the address of the server that hosted
www.foobar.com

What is a server?
	 in my own definition this is a computer, situated in somewere or anywhere and
	 we can communicate with it through internet to access the data stored in it

What is the role of the domain name?
	As we all know, A computer or server can be located through it ip address which is number
	in nature and this as become a challenge for human to adapt with, So having a domain name
	thats point to a address of a certian server makes it easier for human to adapt with.

What type of DNS record www is in www.foobar.com?
	www is typical CNAME record in www.foobar.com.
	it can also be An A record i.e
	www.foobar.com in CNAME foobar.com and
	www.foobar.com in A 8.8.8.8

What is the role web server NGINX?
	It is  used to serve a static file to the client (e.g HTML, CSS, IMG etc..)

What is the role of App server WebSphere?
	It provides a reliable and secure runtime for the simple web stack

What the role of the Database MySql?
	This is used to store data such as users information, and for easy access at anytime needed

what is the server is using to communicate with the computer of the user requesting the website?
	the server is using HTTP to communicate with the user over TCP/IP conection.


Issues with this infastructure
==============================
SPOF: there are multiple single point of failure in this simple web stack
EX: The app server WebSphere if there is any issue with this component the entire site
will be inaccessible.

Downtime: this will ocure most expectially when the Application file is being update.

Too much of incommig trafic can slow dow the server as it can only perfom on
it weighted traffic
