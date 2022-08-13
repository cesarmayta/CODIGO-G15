const {Router} = require('express');
const router = Router();

const {create, auth} = require('../controllers/usuario.controller');

router.route('/')
    .post(create)

router.route('/auth')
    .post(auth)
  
module.exports = router;