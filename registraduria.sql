-- phpMyAdmin SQL Dump
-- version 4.8.3
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 29-05-2019 a las 05:54:05
-- Versión del servidor: 10.1.36-MariaDB
-- Versión de PHP: 7.2.11

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `registraduria`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `files`
--

CREATE TABLE `files` (
  `idfiles` int(11) NOT NULL,
  `ruta` varchar(45) COLLATE utf8_bin DEFAULT NULL,
  `hash` varchar(45) COLLATE utf8_bin DEFAULT NULL,
  `licencia` varchar(255) COLLATE utf8_bin NOT NULL,
  `user_iduser` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

--
-- Volcado de datos para la tabla `files`
--

INSERT INTO `files` (`idfiles`, `ruta`, `hash`, `licencia`, `user_iduser`) VALUES
(6, './files\\Texto.txt', 'dca8d18055390c4bd34cc17b3741ede6', 'Archivo no tiene permiso de uso libre.', 3),
(9, './files\\test.txt.txt', '0ad066a5d29f3f2a2a1c7c17dd082a79', 'Archivo no tiene permiso de uso libre.', 3);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `user`
--

CREATE TABLE `user` (
  `iduser` int(11) NOT NULL,
  `nombres` varchar(45) COLLATE utf8_bin DEFAULT NULL,
  `apellidos` varchar(45) COLLATE utf8_bin DEFAULT NULL,
  `email` varchar(45) COLLATE utf8_bin DEFAULT NULL,
  `password` varchar(45) COLLATE utf8_bin DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

--
-- Volcado de datos para la tabla `user`
--

INSERT INTO `user` (`iduser`, `nombres`, `apellidos`, `email`, `password`) VALUES
(1, 'Esnayder', 'Morales', 'esnaydermorales25@gmail.com', '123456'),
(2, 'Esnayder', 'Morales', 'esnaydermorales25@gmail.com', '6e0a23b6ba9f545e9710e84d6abbbbb7'),
(3, 'Esnayder', 'Morales', 'test@test.com', 'e10adc3949ba59abbe56e057f20f883e');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `files`
--
ALTER TABLE `files`
  ADD PRIMARY KEY (`idfiles`),
  ADD KEY `fk_files_user_idx` (`user_iduser`);

--
-- Indices de la tabla `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`iduser`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `files`
--
ALTER TABLE `files`
  MODIFY `idfiles` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT de la tabla `user`
--
ALTER TABLE `user`
  MODIFY `iduser` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `files`
--
ALTER TABLE `files`
  ADD CONSTRAINT `fk_files_user` FOREIGN KEY (`user_iduser`) REFERENCES `user` (`iduser`) ON DELETE NO ACTION ON UPDATE NO ACTION;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
