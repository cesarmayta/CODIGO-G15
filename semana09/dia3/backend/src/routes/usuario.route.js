const {Router} = require('express');
const router = Router();

const {create} = require('../controllers/usuario.controller');

router.route('/')
    .post(create)
  
module.exports = router;