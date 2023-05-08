const express = require('express');
const app = express();
const cors  = require('core')

app.use(cors())
app.use((req, res, next) => {
  res.header('Access-Control-Allow-Origin', '*');
  res.header('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE');
  res.header('Access-Control-Allow-Headers', 'Content-Type, Authorization');
  next();
});

app.post('/anime', (req, res) => {
  // votre code pour traiter la demande POST
});

app.listen(5000, () => {
  console.log('Serveur en écoute sur le port 5000');
});
