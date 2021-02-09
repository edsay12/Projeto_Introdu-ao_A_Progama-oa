-- --------------------------------------------------------
-- Servidor:                     localhost
-- Versão do servidor:           5.7.24 - MySQL Community Server (GPL)
-- OS do Servidor:               Win32
-- HeidiSQL Versão:              10.2.0.5599
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

-- Copiando dados para a tabela introduçaoaprogamaçao.clientes: ~1 rows (aproximadamente)
/*!40000 ALTER TABLE `clientes` DISABLE KEYS */;
INSERT INTO `clientes` (`id_clientes`, `nome`, `cpf`, `endereço`, `complemento`, `telefone`, `Dia_cadastro`) VALUES
	(1, 'lucio', '123121251251', 'rua rio bahia', 'd', '8198354012', '2021-02-08 20:38:39');
/*!40000 ALTER TABLE `clientes` ENABLE KEYS */;

-- Copiando dados para a tabela introduçaoaprogamaçao.produtos: ~6 rows (aproximadamente)
/*!40000 ALTER TABLE `produtos` DISABLE KEYS */;
INSERT INTO `produtos` (`id_produtos`, `nome`, `tipo`, `quantidade`, `valor`, `marca`, `data_atualizaçao`) VALUES
	(2, 'coca', 'Equipamentos', 12, 12, 'ret', '2021-02-07 15:42:07'),
	(3, 'coca', 'Equipamentos', 12, 12, 'ret', '2021-02-07 15:42:07'),
	(4, 'coca', 'Equipamentos', 15, 14, 'ret', '2021-02-07 15:42:07'),
	(10, 'jurubeba25', 'Informatica', 21, 50, 'sony', '2021-02-07 16:19:47');
/*!40000 ALTER TABLE `produtos` ENABLE KEYS */;

-- Copiando dados para a tabela introduçaoaprogamaçao.usuarios: ~2 rows (aproximadamente)
/*!40000 ALTER TABLE `usuarios` DISABLE KEYS */;
INSERT INTO `usuarios` (`id_usuarios`, `nome`, `sobrenome`, `email`, `logim`, `senha`, `datacriaçao`, `dataatualizaçao`) VALUES
	(40, 'lucas', 'silva1212', 'edvandearaujo2@hotmial.com', 'edsay12', '123', '2021-02-07 16:11:36', '2021-02-08 20:47:32'),
	(41, 'davi', 'silva', 'edvandearaujo2@hotmail.com', 'davigolias', '123', '2021-02-07 16:19:18', '2021-02-07 16:19:18');
/*!40000 ALTER TABLE `usuarios` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
