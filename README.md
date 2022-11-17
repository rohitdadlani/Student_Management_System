# Student_Management_System




These are my api endpoints for the application:


![Screenshot from 2022-11-17 11-56-30](https://user-images.githubusercontent.com/84759010/202374106-e04601f7-dfa7-4212-8c78-78522feea1e2.png)




This is the homepage of the application
In ths page it was showing the urls that are available.


![Screenshot from 2022-11-17 11-58-24](https://user-images.githubusercontent.com/84759010/202374253-3257a11f-49f5-4321-8dfa-7f7356ec3079.png)



When we hit the path http://127.0.0.1:5000/api/users/  then it will redirect to users api
Here this page given that the login credentials is not provided that's why we have to login first.


![Screenshot from 2022-11-17 12-00-18](https://user-images.githubusercontent.com/84759010/202374266-72bf98d8-6a17-433f-ac2e-83676db82f44.png)




Click on the login button that was availabe in the top right and login with credentials.
That will give this page

![Screenshot from 2022-11-17 12-02-03](https://user-images.githubusercontent.com/84759010/202374284-f37208cf-9747-4abd-a89b-0d6238785b2e.png)




After login details were given then the users api will shows the available users in the application

![Screenshot from 2022-11-17 12-03-30](https://user-images.githubusercontent.com/84759010/202374289-b9ccab5d-1f04-4f8d-9a6f-73e66d7180c5.png)




Now lets move to the attendence section
While hitting the url http://127.0.0.1:5000/api/attendence/ if you are login then it will shows the attendence with the student details.

![Screenshot from 2022-11-17 12-03-50](https://user-images.githubusercontent.com/84759010/202374300-863ed28d-f4cd-41cf-b9af-90a6be1fe





From here we can add the different student attendence also on the same url.

![Screenshot from 2022-11-17 12-04-52](https://user-images.githubusercontent.com/84759010/202374308-e47117fc-aebe-4018-8fbc-17e5ee4b1c55.png)
afc.png)





![Screenshot from 2022-11-17 12-05-10](https://user-images.githubusercontent.com/84759010/202374376-beaef564-8f4b-4fe5-933b-0cab3bc57d00.png)





Now we are moving to the new feature of the application
We have added a table of the category where we can put the Present and Absent option to the dropdown menu in the attendence table
Url http://127.0.0.1:5000/api/category/

For now I have already added the Present and Absent option only. But in future if the requirement is there then we can add more categories also

![Screenshot from 2022-11-17 12-06-02](https://user-images.githubusercontent.com/84759010/202374386-7a56414b-430d-450c-a1f5-75ee4a7cedf6.png)





While in the same url as we mentioned above we can add the category by simply add the name of the category and post it.

If you are login then only we can get this otherwise it will not show the post option.

If we add the category from here then it will directly redirect to the attendence api. via Foreign key


![Screenshot from 2022-11-17 12-06-27](https://user-images.githubusercontent.com/84759010/202374408-96f63292-18bd-44a1-8875-879a98d869ed.png)
