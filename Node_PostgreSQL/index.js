const express = require('express');
const bodyParser = require('body-parser');
const { Pool } = require('pg');
const path = require('path');
const app = express();
const port = 3000;

const pool = new Pool({
  user: 'postgres',
  host: 'localhost',
  database: 'crud_usuarios',
  password: '12345',
  port: 5432,
});

app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());

app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, '..', 'index.html'));
});

app.get('/usuarios', async (req, res) => {
  try {
    const result = await pool.query('SELECT * FROM usuarios ORDER BY id DESC');
    res.json(result.rows.map(u => ({
      _id: u.id,
      nombre: u.nombre,
      email: u.email
    })));
  } catch (err) {
    console.error('Error al obtener usuarios:', err); 
    res.status(500).json({ error: 'Error al obtener usuarios' });
  }
});

app.post('/crear', async (req, res) => {
  const { nombre, email } = req.body;
  try {
    await pool.query('INSERT INTO usuarios (nombre, email) VALUES ($1, $2)', [nombre, email]);
    res.redirect('/');
  } catch (err) {
    res.status(500).send('Error al crear usuario');
  }
});

app.post('/eliminar/:id', async (req, res) => {
  const { id } = req.params;
  try {
    await pool.query('DELETE FROM usuarios WHERE id = $1', [id]);
    res.redirect('/');
  } catch (err) {
    res.status(500).send('Error al eliminar usuario');
  }
});

app.post('/actualizar/:id', async (req, res) => {
  const { id } = req.params;
  const { nombre, email } = req.body;
  try {
    await pool.query('UPDATE usuarios SET nombre = $1, email = $2 WHERE id = $3', [nombre, email, id]);
    res.redirect('/');
  } catch (err) {
    res.status(500).send('Error al actualizar usuario');
  }
});


app.listen(port, () => {
  console.log(`Servidor corriendo en http://localhost:${port}`);
});
