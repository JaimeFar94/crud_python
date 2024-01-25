-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 03-01-2024 a las 05:50:41
-- Versión del servidor: 10.4.25-MariaDB
-- Versión de PHP: 8.1.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `medico`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `antecedentes`
--

CREATE TABLE `antecedentes` (
  `diabetes` varchar(20) DEFAULT NULL,
  `hipertension` varchar(20) DEFAULT NULL,
  `artritis` varchar(20) DEFAULT NULL,
  `alergia` varchar(20) DEFAULT NULL,
  `catarata` varchar(20) DEFAULT NULL,
  `glaucoma` varchar(20) DEFAULT NULL,
  `estrabismo` varchar(20) DEFAULT NULL,
  `queratocono` varchar(20) DEFAULT NULL,
  `otros` varchar(50) DEFAULT NULL,
  `diabetes_per` varchar(20) DEFAULT NULL,
  `hipertension_per` varchar(20) DEFAULT NULL,
  `Artritis_per` varchar(20) DEFAULT NULL,
  `Alergia_per` varchar(20) DEFAULT NULL,
  `ulcera_per` varchar(20) DEFAULT NULL,
  `cirugia_per` varchar(20) DEFAULT NULL,
  `lentes_contacto_per` varchar(20) DEFAULT NULL,
  `otros1` varchar(20) DEFAULT NULL,
  `descripcion` varchar(80) DEFAULT NULL
);

--
-- Volcado de datos para la tabla `antecedentes`
--

INSERT INTO `antecedentes` (`diabetes`, `hipertension`, `artritis`, `alergia`, `catarata`, `glaucoma`, `estrabismo`, `queratocono`, `otros`, `diabetes_per`, `hipertension_per`, `Artritis_per`, `Alergia_per`, `ulcera_per`, `cirugia_per`, `lentes_contacto_per`, `otros1`, `descripcion`, `paciente_documento`) VALUES
('no_refiere', 'no_refiere', 'no_refiere', 'no_refiere', 'no_refiere', 'no_refiere', 'no_refiere', 'no_refiere', 'No Refiere', 'SI', 'si', 'no', 'no', 'no', 'no', 'no', 'no', 'No tiene', NULL),
('no_refiere', 'no_refiere', 'no_refiere', 'no_refiere', 'no_refiere', 'no_refiere', 'no_refiere', 'no_refiere', 'No Refiere', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', NULL),
('no_refiere', 'no_refiere', 'no_refiere', 'no_refiere', 'no_refiere', 'no_refiere', 'no_refiere', 'no_refiere', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', NULL),
('refiere', 'no_refiere', 'no_refiere', 'no_refiere', 'no_refiere', 'refiere', 'no_refiere', 'refiere', 'No Refiere', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', NULL),
('No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'Ninguna', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'Ninguno', 'Sin descripción', 1),
('refiere', 'refiere', 'no_refiere', 'no_refiere', 'no_refiere', 'no_refiere', 'refiere', 'refiere', 'No Refiere', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', NULL),
('no_refiere', 'no_refiere', 'no_refiere', 'no_refiere', 'no_refiere', 'no_refiere', 'no_refiere', 'no_refiere', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', NULL),
('no_refiere', 'no_refiere', 'no_refiere', 'no_refiere', 'no_refiere', 'no_refiere', 'no_refiere', 'no_refiere', 'No Refiere', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', NULL),
('no_refiere', 'no_refiere', 'no_refiere', 'no_refiere', 'no_refiere', 'no_refiere', 'no_refiere', 'no_refiere', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', NULL);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `login`
--

CREATE TABLE `login` (
  `nombre` varchar(30) DEFAULT NULL,
  `Correo` varchar(70) DEFAULT NULL,
  `Clinica` varchar(60) DEFAULT NULL,
  `usuario` varchar(50) DEFAULT NULL,
  `contraseña` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `login`
--

INSERT INTO `login` (`nombre`, `Correo`, `Clinica`, `usuario`, `contraseña`) VALUES
('Jaime Farfan', 'jaime.farfan@cun.edu.co', 'Ojitos S.A', 'j-far', 'Jaime2581895');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `mov_consulta`
--

CREATE TABLE `mov_consulta` (
  `mov_consulta` varchar(200) DEFAULT NULL,
  `ulti_consulta` varchar(100) DEFAULT NULL,
  `esfera` varchar(50) DEFAULT NULL,
  `cilindro` varchar(50) DEFAULT NULL,
  `eje` varchar(50) DEFAULT NULL,
  `dp` varchar(50) DEFAULT NULL,
  `vl20` varchar(50) DEFAULT NULL,
  `vp20` varchar(50) DEFAULT NULL,
  `add_0` varchar(50) DEFAULT NULL,
  `esfera_1` varchar(50) DEFAULT NULL,
  `cilindro_1` varchar(50) DEFAULT NULL,
  `eje_1` varchar(50) DEFAULT NULL,
  `dp_1` varchar(50) DEFAULT NULL,
  `vl20_1` varchar(50) DEFAULT NULL,
  `vp20_1` varchar(50) DEFAULT NULL,
  `add_1` varchar(50) DEFAULT NULL,
  `tipo_lente` varchar(50) DEFAULT NULL,
  `montura` varchar(50) DEFAULT NULL,
  `material` varchar(50) DEFAULT NULL,
  `filtro` varchar(50) DEFAULT NULL,
  `color` varchar(50) DEFAULT NULL,
  `observacion` varchar(100) DEFAULT NULL
);

--
-- Volcado de datos para la tabla `mov_consulta`
--

INSERT INTO `mov_consulta` (`mov_consulta`, `ulti_consulta`, `esfera`, `cilindro`, `eje`, `dp`, `vl20`, `vp20`, `add_0`, `esfera_1`, `cilindro_1`, `eje_1`, `dp_1`, `vl20_1`, `vp20_1`, `add_1`, `tipo_lente`, `montura`, `material`, `filtro`, `color`, `observacion`, `paciente_documento`) VALUES
('Ardor en Ojos', '4/11/2023', 'curva', 'negro', 'normal', '20', '25', 'normal', 'normal', 'curva', 'negro', 'normal', '20', '25', 'normal', 'normal', 'bueno', 'buena', 'plastico', 'transition', 'azul', 'ninguna', NULL),
('', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', NULL),
('Ojito maluco', 'No tuvo', 'curva', 'bien', 'normal', 'normal', 'normal', 'normal', 'normal', 'curva', 'bien', 'normal', 'normal', 'normal', 'normal', 'normal', 'bueno', 'buena', 'plastico', 'transition', 'rosa', 'ninguna', NULL),
('Ojito maluco', '4/11/2023', 'curva', 'curva', 'curva', 'curva', 'curva', 'curva', 'curva', 'curva', 'curva', 'curva', 'curva', 'curva', 'curva', 'curva', 'Ojito maluco', 'buena', 'plastico', 'transition', 'rojo', 'ninguna', NULL),
('Ardor en Ojos', '4/11/2023', 'curva', 'curva', 'curva', 'curva', 'curva', 'curva', 'curva', 'curva', 'curva', 'curva', 'curva', 'curva', 'curva', 'curva', 'bueno', 'fina', 'plastico', 'transition', 'rosa', 'ninguna', NULL),
('Ojito maluco', '4/11/2023', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'bueno', 'fina', 'plastico', 'transition', 'rojo', 'ninguna', NULL),
('Ojito maluco', '4/11/2023', 'NO', 'NO', 'NO', 'NO', 'NO', 'NONO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'bueno', 'fina', 'plastico', 'transition', 'rojo', 'ninguna', NULL),
('Ojito maluco', '4/11/2023', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'bueno', 'fina', 'plastico', 'transition', 'rojo', 'ninguna', NULL);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `pacientes`
--

CREATE TABLE `pacientes` (
  `documento` int(11) NOT NULL,
  `tipo` varchar(10) DEFAULT NULL,
  `nombre` varchar(200) DEFAULT NULL,
  `edad` int(11) DEFAULT NULL,
  `genero` varchar(50) DEFAULT NULL,
  `correo_electronico` varchar(255) DEFAULT NULL,
  `direccion` text DEFAULT NULL,
  `telefono` varchar(40) DEFAULT NULL,
  `eps` varchar(50) DEFAULT NULL,
  `cargo` varchar(100) DEFAULT NULL,
  `acompanante` varchar(100) DEFAULT 'Sin acompañante',
  `parentesco` varchar(60) DEFAULT NULL,
  `telefono_acompanante` varchar(50) DEFAULT NULL,
  `motivo_consulta` text DEFAULT NULL,
  `ultima_revision` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `pacientes`
--

INSERT INTO `pacientes` (`documento`, `tipo`, `nombre`, `edad`, `genero`, `correo_electronico`, `direccion`, `telefono`, `eps`, `cargo`, `acompanante`, `parentesco`, `telefono_acompanante`, `motivo_consulta`, `ultima_revision`, `foto`) VALUES
(1, 'CC', 'Juan Pérez', 30, 'Masculino', 'juan.perez@email.com', 'Calle 123', '123456789', 'EPS-Salud', 'Empleado', 'Ana Pérez', 'Familiar', '987654321', 'Problemas de visión', '2023-12-01 10:00:00', 'juan.jpg'),
(1019103000, 'cedula', 'Jaime Rodriguez', 29, 'Masculino', 'farfanjaime05@gmail.com', 'cra53b#135a12', '3204978155', 'salud total', 'Ingeniero en sistemas', 'Gloria Rodriguez', 'Madre', '3152805686', 'Ojos malucos', '2023-11-30 00:00:00', '<FileStorage: \'AcerolaEmote.png\' (\'image/png\')>');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `vista`
--

CREATE TABLE `vista` (
  `vision_lejana` varchar(40) DEFAULT NULL,
  `vision_proxima` varchar(40) DEFAULT NULL,
  `duccion_od` varchar(40) DEFAULT NULL,
  `duccion_oi` varchar(40) DEFAULT NULL,
  `ppc_od` varchar(40) DEFAULT NULL,
  `ppc_oi` varchar(40) DEFAULT NULL,
  `ojo_derecho` varchar(30) DEFAULT NULL,
  `ojo_izquierdo` varchar(30) DEFAULT NULL,
  `ojo_drc_querato` varchar(30) DEFAULT NULL,
  `ojo_izq_querato` varchar(30) DEFAULT NULL,
  `ojo_drc_refac` varchar(30) DEFAULT NULL,
  `ojo_izq_refac` varchar(30) DEFAULT NULL,
  `esfera_retino` varchar(30) DEFAULT NULL,
  `cilindro_retino` varchar(30) DEFAULT NULL,
  `eje_retino` varchar(30) DEFAULT NULL,
  `dp_retino` varchar(30) DEFAULT NULL,
  `vl20_retino` varchar(30) DEFAULT NULL,
  `vp20_retino` varchar(30) DEFAULT NULL,
  `add_retino` varchar(30) DEFAULT NULL,
  `esfera_retino_1` varchar(30) DEFAULT NULL,
  `cilindro_retino_1` varchar(30) DEFAULT NULL,
  `eje_retino_1` varchar(30) DEFAULT NULL,
  `dp_retino_1` varchar(30) DEFAULT NULL,
  `vl20_retino_1` varchar(30) DEFAULT NULL,
  `vp20_retino_1` varchar(30) DEFAULT NULL,
  `add_retino_1` varchar(30) DEFAULT NULL
) ;

--
-- Volcado de datos para la tabla `vista`
--

INSERT INTO `vista` (`vision_lejana`, `vision_proxima`, `duccion_od`, `duccion_oi`, `ppc_od`, `ppc_oi`, `ojo_derecho`, `ojo_izquierdo`, `ojo_drc_querato`, `ojo_izq_querato`, `ojo_drc_refac`, `ojo_izq_refac`, `esfera_retino`, `cilindro_retino`, `eje_retino`, `dp_retino`, `vl20_retino`, `vp20_retino`, `add_retino`, `esfera_retino_1`, `cilindro_retino_1`, `eje_retino_1`, `dp_retino_1`, `vl20_retino_1`, `vp20_retino_1`, `add_retino_1`, `paciente_documento`) VALUES
('mucha', 'poca', 'NO', 'NO', 'NO', 'NO', 'bien', 'mal', 'mal', 'bien', 'mal', 'mal', 'curva', 'Ojito maluco', 'normal', 'Ojito maluco', 'Ojito maluco', 'Ojito maluco', 'SI', 'curva', 'Ojito maluco', 'normal', 'Ojito maluco', 'Ojito maluco', 'Ojito maluco', 'NO', NULL),
('', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', NULL),
('mucha', 'poca', 'NO', 'NO', 'NO', 'NO', 'bien', 'mal', 'mal', 'bien', 'mal', 'mal', 'Ojito maluco', 'normal', 'normal', 'curva', 'normal', 'normal', 'normal', 'Ojito maluco', 'normal', 'normal', 'curva', 'normal', 'normal', 'normal', NULL),
('mucha', 'poca', 'NO', 'NO', 'NO', 'NO', 'bien', 'mal', 'mal', 'bien', 'mal', 'bien', 'curva', 'curva', 'curva', 'curva', 'curva', 'curva', 'curva', 'curva', 'curva', 'curva', 'curva', 'curva', 'curva', 'curva', NULL),
('mucha', 'poca', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NONO', 'NO', 'NO', 'NO', NULL),
('NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', NULL),
('mucha', 'mucha', 'mucha', 'mucha', 'mucha', 'mucha', 'mucha', 'mucha', 'mucha', 'mucha', 'mucha', 'mucha', 'mucha', 'mucha', 'mucha', 'mucha', 'mucha', 'mucha', 'mucha', 'mucha', 'mucha', 'mucha', 'mucha', 'mucha', 'mucha', 'mucha', NULL),
('no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'nono', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', NULL);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `antecedentes`
--
ALTER TABLE `antecedentes`
  ADD KEY `fk_paciente_documento_idx` (`paciente_documento`,`diabetes`) USING BTREE;

--
-- Indices de la tabla `mov_consulta`
--
ALTER TABLE `mov_consulta`
  ADD KEY `fk_consulta_documento_idx` (`paciente_documento`) USING BTREE;

--
-- Indices de la tabla `pacientes`
--
ALTER TABLE `pacientes`
  ADD PRIMARY KEY (`documento`);

--
-- Indices de la tabla `vista`
--
ALTER TABLE `vista`
  ADD KEY `fk_paciente_documento_idx` (`paciente_documento`);

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `antecedentes`
--
ALTER TABLE `antecedentes`
  ADD CONSTRAINT `antecedentes_ibfk_1` FOREIGN KEY (`paciente_documento`) REFERENCES `pacientes` (`documento`);

--
-- Filtros para la tabla `mov_consulta`
--
ALTER TABLE `mov_consulta`
  ADD CONSTRAINT `mov_consulta_ibfk_1` FOREIGN KEY (`paciente_documento`) REFERENCES `pacientes` (`documento`);

--
-- Filtros para la tabla `vista`
--
ALTER TABLE `vista`
  ADD CONSTRAINT `vista_ibfk_1` FOREIGN KEY (`paciente_documento`) REFERENCES `pacientes` (`documento`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
