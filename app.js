const express = require('express');
const mysql = require('mysql');
const bodyParser = require('body-parser');
const app = express();


app.use(bodyParser.json());

const connection = mysql.createConnection({
    host: 'localhost',
    user: 'root',
    password: '',
    database: 'micro-db',
    port: '3306',
});

connection.connect();

// Check if the users table exists; if not, create it
const createTableQuery = `
    CREATE TABLE IF NOT EXISTS users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        first_name VARCHAR(255),
        last_name VARCHAR(255),
        email VARCHAR(255),
        gender VARCHAR(10),
        ip_address VARCHAR(15)
    )
`;

connection.query(createTableQuery, (error) => {
    if (error) {
        console.error('Error creating users table:', error);
    } else {
        console.log('Users table is ready.');
    }
});

// Get all users
app.get('/users', (req, res) => {
    const query = 'SELECT id, first_name, last_name, email, gender, ip_address FROM users';

    connection.query(query, (error, results) => {
        if (error) {
            console.error('Error fetching all users:', error);
            res.status(500).json({ error: 'Internal Server Error' });
        } else {
            res.json(results);
        }
    });
});

// Get user by ID
app.get('/user/:userId', (req, res) => {
    const userId = req.params.userId;
    const query = 'SELECT id, first_name, last_name, email, gender, ip_address FROM users WHERE id = ?';

  connection.query(query, [userId], (error, results) => {
        if (error) {
    console.error('Error executing query:', query);
    console.error('Error fetching user by ID:', error);
    res.status(500).json({ error: 'Internal Server Error' });
        } else if (results.length > 0) {
            res.json(results[0]);
        } else {
            res.status(404).json({ error: 'User not found' });
        }
    });
});
// Add a new user
app.post('/user', (req, res) => {
    const newUser = req.body;
const query = 'INSERT INTO users SET ?';
connection.query(query, [newUser], (error, results) => {
       if (error) {
    console.error('Error executing query:', query);
    console.error('Error adding new user:', error);
    res.status(500).json({ error: 'Internal Server Error' });
} else {
            res.status(201).json({ message: 'User added successfully', userId: results.insertId });
        }
    });
});


module.exports = app;