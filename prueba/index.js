import express from 'express';
import { Pool } from 'pg';

const app = express();
const port = process.env.PORT || 3000;

if (!process.env.DATABASE_URL) {
  console.error('DATABASE_URL no está definido');
  process.exit(1);
}

const pool = new Pool({
  connectionString: process.env.DATABASE_URL,
  max: 20,
  idleTimeoutMillis: 30000,
  connectionTimeoutMillis: 2000,
});

app.use(express.json());

app.get('/', async (req, res) => {
  try {
    const result = await pool.query('SELECT NOW() as ahora');
    res.json({
      mensaje: 'Conexión OK',
      hora_bd: result.rows[0].ahora
    });
  } catch (err) {
    console.error('Error en base de datos:', err);
    res.status(500).json({ error: 'Error en la base de datos' });
  }
});

const server = app.listen(port, '0.0.0.0', () => {
  console.log(`Servidor escuchando en puerto ${port}`);
});

process.on('SIGTERM', async () => {
  console.log('SIGTERM recibido, cerrando gracefully...');
  server.close(async () => {
    await pool.end();
    process.exit(0);
  });
});