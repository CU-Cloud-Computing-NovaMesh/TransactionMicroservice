const express = require('express');
const swaggerUi = require('swagger-ui-express');
const YAML = require('yamljs');
const path = require('path');

const app = express();

app.use(express.json());

const swaggerDocument = YAML.load(path.join(__dirname, 'api', 'openapi.yaml'));

app.use('/api-docs', swaggerUi.serve, swaggerUi.setup(swaggerDocument));

app.get('/', (req, res) => {
  res.send('TransactionMicroservice is running');
});


const PORT = process.env.PORT || 5050;
app.listen(PORT, () => console.log(`Running on http://localhost:${PORT}/api-docs`));
