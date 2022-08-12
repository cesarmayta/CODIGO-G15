const {Router} = require('express');
const router = Router();

const {getAll} = require('../controllers/tarea.constroller');

router.route('/')
    .get(getAll)

module.exports = router;