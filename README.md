# CS 340 Portfolio Reflection

## Maintainable, Readable, and Adaptable Programs

I write programs that are maintainable, readable, and adaptable by organizing my code into clear sections, using meaningful variable names, and separating major responsibilities into different files or functions. In Project One, I created a CRUD Python module that handled database operations for MongoDB. This made the code easier to maintain because the database connection and CRUD methods were stored in one reusable module instead of being repeated throughout the dashboard code.

Using the CRUD module in Project Two was helpful because the dashboard could focus on the user interface, filters, table, charts, and map, while the module handled database communication. This made the project more organized and easier to update. In the future, this CRUD module could be reused in other applications that need to connect to the Austin Animal Center database or another MongoDB collection. For example, it could be used in a mobile app, a reporting tool, or another dashboard that tracks shelter animals.

## My Approach as a Computer Scientist

When I approach a problem as a computer scientist, I first review the client requirements and break the problem into smaller parts. For the Grazioso Salvare dashboard, I identified the required data, the rescue-type filters, the database queries, and the dashboard widgets that needed to update dynamically. I then worked step by step by connecting MongoDB, testing the CRUD module, building the dashboard layout, adding filter logic, and testing each dashboard feature.

This project was different from previous assignments because it required me to connect multiple parts of a full-stack application. I had to work with the database, Python code, dashboard components, and user interaction all in one project. In future database projects, I would use the same strategy of starting with the client requirements, designing the database queries first, testing each part separately, and then connecting the pieces together into a complete application.

## What Computer Scientists Do and Why It Matters

Computer scientists design and build solutions that help people solve problems using technology. They analyze requirements, organize data, write software, test systems, and improve how users interact with information. This matters because well-designed software can help organizations make faster and better decisions.

For a company like Grazioso Salvare, this dashboard can make their work more efficient by helping them quickly identify dogs that match specific rescue-training profiles. Instead of manually searching through animal records, users can select a rescue type and immediately see matching animals, breed information, and location data. This helps the organization save time, reduce errors, and focus more on training rescue animals that can help people in emergency situations.
