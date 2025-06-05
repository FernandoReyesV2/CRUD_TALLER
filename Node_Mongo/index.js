const express = require('express');
const mongoose = require('mongoose');
const dotenv = require('dotenv');
const path = require('path');

dotenv.config();
const app = express();
const PORT = 3000;

app.use(express.urlencoded({ extended: true }));
app.use(express.json());

const usuarioSchema = new mongoose.Schema({
  nombre: String,
  email: String,
});
const Usuario = mongoose.model('Usuario', usuarioSchema);

app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, '..', 'index.html'));
});

app.get('/usuarios', async (req, res) => {
  const usuarios = await Usuario.find();
  res.json(usuarios);
});

app.post('/crear', async (req, res) => {
  const { nombre, email } = req.body;
  await Usuario.create({ nombre, email });
  res.redirect('/');
});

app.post('/eliminar/:id', async (req, res) => {
  await Usuario.findByIdAndDelete(req.params.id);
  res.redirect('/');
});

app.post('/actualizar/:id', async (req, res) => {
  const { nombre, email } = req.body;
  await Usuario.findByIdAndUpdate(req.params.id, { nombre, email });
  res.redirect('/');
});

mongoose.connect(process.env.MONGO_URI)
  .then(() => {
    console.log('Conectado a MongoDB');
    app.listen(PORT, () => console.log(`🚀 Servidor en http://localhost:${PORT}`));
  })
  .catch(err => console.error('Error conectando a MongoDB:', err));
