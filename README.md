# Video-Game-Wishlist
A wishlist page for users who have signed in to create their own private wishlist of video games. 

## :computer: [Click here](https://video-game-wishlist.onrender.com/) to see my live project!

## :page_facing_up: About
- A web app which allows users who have signed in to add games and mark them as wishlisted, allowing them to keep track of which games they would like to obtain or play in the future. It has multiple pages designed for ease of use, a main page which shows every game, a private wishlist page which is private to each user, a search bar to search for a specific game thats already in the database, and a page for the user to add a new game to the database.

## :pencil2: Planning & Problem Solving
- Created a wireframe to plan the page layout and to assist with planned functionality of certain aspects of the page.
![First Wireframe picture](./wireframe.png)
- When planning I created a wireframe as a base template for the home page, then as the task progressed I realized I would need to create further wireframes to help me with my layouts for my new game page.
![Second Wireframe Picture](./Wireframe1.png)
- Initially when building my project I had a serious issue where on the initial page load it couldn't find the index, I'd checked all my routes and made sure they were loading the correct page but it still couldn't find it, eventually after some investigation I discovered that the initial index page had a prefix applied to it, so it wouldn't load initially as there's no prefix when you first load the page.
- When making my data display on the wishlist page, I had an issue where it would display every game for every users wishlist. After inspecting my method for getting the wishlisted games, I realised I had used the wrong method to access them, and so I had to change the method, instead of getting all games, I made an extra table containing the users id and the games id, this allowed me to link each user with specific games and so on the wishlist page I was able to use that to display only games that the logged in user was linked to via that additional table.

## :star2: Potential Improvements
- On the main page where all games are listed, It would be easier to use the page if the user is able to see which games they have already wishlisted

## :rocket: Cool tech
- The wishlist page for the site is only viewable by a logged in user, and will only display wishlisted games for that specific user
- The user is able to edit their account details including their password if they wish

## :beetle: Bugs to fix
- 

## :notebook: Lessons learnt
- When creating the routes for a web app, make sure the index page does not have a url prefix to avoid the page being unable to find it.

## :white_check_mark: Future Features
- 