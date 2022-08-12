-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 09-08-2022 a las 22:50:33
-- Versión del servidor: 10.4.22-MariaDB
-- Versión de PHP: 7.4.27

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `isynerg`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `actividades_maquina`
--

CREATE TABLE `actividades_maquina` (
  `id` int(11) NOT NULL,
  `maquina_id` int(11) NOT NULL,
  `azul` int(11) DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `actividades_maquina`
--

INSERT INTO `actividades_maquina` (`id`, `maquina_id`, `azul`, `created_at`, `updated_at`) VALUES
(1, 1, 100, '2022-08-04 16:54:02', '2022-08-04 16:54:02'),
(2, 1, 6, '2022-08-04 17:12:04', '2022-08-04 17:12:04'),
(3, 1, 0, '2022-08-04 17:20:33', '2022-08-04 17:20:33'),
(4, 1, 2, '2022-08-04 17:31:19', '2022-08-04 17:31:19'),
(5, 1, 3, '2022-08-04 17:33:13', '2022-08-04 17:33:13'),
(6, 1, 4, '2022-08-04 17:34:08', '2022-08-04 17:34:08'),
(7, 1, 6, '2022-08-05 21:33:04', '2022-08-05 21:33:04'),
(8, 1, 0, '2022-08-08 22:49:41', '2022-08-08 22:49:41');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `actividades_usuario`
--

CREATE TABLE `actividades_usuario` (
  `id` int(11) NOT NULL,
  `usuario_id` int(11) NOT NULL,
  `verde` int(11) DEFAULT NULL,
  `amarillo` int(11) DEFAULT NULL,
  `morado` int(11) DEFAULT NULL,
  `rojo` int(11) DEFAULT NULL,
  `produccion_real` int(11) DEFAULT NULL,
  `piezas_malas` int(11) DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NULL DEFAULT current_timestamp(),
  `maquina_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `actividades_usuario`
--

INSERT INTO `actividades_usuario` (`id`, `usuario_id`, `verde`, `amarillo`, `morado`, `rojo`, `produccion_real`, `piezas_malas`, `created_at`, `updated_at`, `maquina_id`) VALUES
(1, 1, 20000, 20, 20, 20, 1000, 140, '2022-08-03 22:01:54', '2022-08-03 22:01:54', 1),
(2, 1, 40000, 200, 2, 1, 6000, 11, '2022-08-04 15:11:38', '2022-08-04 15:11:38', 1),
(3, 1, 40000, 200, 2, 1, 11, 11, '2022-08-04 15:17:11', '2022-08-04 15:17:11', 1),
(4, 1, 60000, 300, 3, 1, 4000, 11, '2022-08-03 15:31:53', '2022-08-03 15:31:53', 1),
(5, 1, 0, 1555, 0, 1, 11, 11, '2022-07-04 15:32:22', '2022-08-04 15:32:22', 1),
(6, 1, 2, 2, 2, 1, 11, 11, '2022-07-04 15:42:58', '2022-08-04 15:42:58', 1),
(7, 1, 19, 19, 19, 3, 11, 11, '2022-07-04 15:44:26', '2022-08-04 15:44:26', 1),
(8, 1, 3, 0, 0, 0, 11, 11, '2022-07-04 15:56:53', '2022-08-04 15:56:53', 1),
(9, 1, 9, 4, 0, 3, 11, 11, '2022-07-04 16:36:06', '2022-08-04 16:36:06', 1),
(16, 1, 600, 4000, 400, 400, 9000, 11, '2022-08-05 21:33:04', '2022-08-05 21:33:04', 1),
(17, 1, 23, 0, 0, 0, 11, 11, '2022-08-08 22:49:41', '2022-08-08 22:49:41', NULL);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `maquina`
--

CREATE TABLE `maquina` (
  `id` int(11) NOT NULL,
  `maquina_mid` int(11) DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `maquina`
--

INSERT INTO `maquina` (`id`, `maquina_mid`, `created_at`, `updated_at`) VALUES
(1, 1, '2022-08-04 16:53:26', '2022-08-04 16:53:26');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `semana_operaciones_maquina`
--

CREATE TABLE `semana_operaciones_maquina` (
  `id` int(11) NOT NULL,
  `maquina_id` int(11) NOT NULL,
  `lunes` int(11) DEFAULT NULL,
  `martes` int(11) DEFAULT NULL,
  `miercoles` int(11) DEFAULT NULL,
  `jueves` int(11) DEFAULT NULL,
  `viernes` int(11) DEFAULT NULL,
  `sabado` int(11) DEFAULT NULL,
  `domingo` int(11) DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `semana_operaciones_maquina`
--

INSERT INTO `semana_operaciones_maquina` (`id`, `maquina_id`, `lunes`, `martes`, `miercoles`, `jueves`, `viernes`, `sabado`, `domingo`, `created_at`, `updated_at`) VALUES
(1, 1, 12, 12, 12, 12, 12, 12, 12, '2022-08-04 17:00:17', '2022-08-04 17:00:17');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `session`
--

CREATE TABLE `session` (
  `id` int(11) NOT NULL,
  `usuario_id` int(11) NOT NULL,
  `fecha` timestamp NULL DEFAULT current_timestamp(),
  `created_at` timestamp NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `session`
--

INSERT INTO `session` (`id`, `usuario_id`, `fecha`, `created_at`, `updated_at`) VALUES
(1, 1, '2022-08-04 17:20:28', '2022-08-04 17:20:28', '2022-08-04 17:20:28'),
(2, 1, '2022-08-04 17:27:21', '2022-08-04 17:27:21', '2022-08-04 17:27:21'),
(3, 13, '2022-08-04 17:27:57', '2022-08-04 17:27:57', '2022-08-04 17:27:57'),
(4, 14, '2022-08-04 17:31:02', '2022-08-04 17:31:02', '2022-08-04 17:31:02'),
(5, 14, '2022-08-04 17:32:51', '2022-08-04 17:32:51', '2022-08-04 17:32:51'),
(6, 1, '2022-08-05 21:32:24', '2022-08-05 21:32:24', '2022-08-05 21:32:24'),
(7, 1, '2022-08-05 21:33:31', '2022-08-05 21:33:31', '2022-08-05 21:33:31'),
(8, 1, '2022-08-08 22:49:11', '2022-08-08 22:49:11', '2022-08-08 22:49:11'),
(9, 1, '2022-08-08 22:54:59', '2022-08-08 22:54:59', '2022-08-08 22:54:59'),
(10, 1, '2022-08-09 16:03:39', '2022-08-09 16:03:39', '2022-08-09 16:03:39');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuarios`
--

CREATE TABLE `usuarios` (
  `id` int(11) NOT NULL,
  `nombre` varchar(50) DEFAULT NULL,
  `password` varchar(50) DEFAULT NULL,
  `dni` varchar(10) DEFAULT NULL,
  `isAdmin` tinyint(4) DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `usuarios`
--

INSERT INTO `usuarios` (`id`, `nombre`, `password`, `dni`, `isAdmin`, `created_at`, `updated_at`) VALUES
(1, 'cristian', '123456', '74309887', 1, '2022-07-26 14:52:17', '2022-07-26 14:52:17'),
(2, 'carlos', '123456', '7456123', 1, '2022-07-26 15:16:39', '2022-07-26 15:16:39'),
(4, NULL, NULL, '77777', NULL, '2022-07-26 20:41:14', '2022-07-26 20:41:14'),
(5, NULL, NULL, '777772', NULL, '2022-07-26 20:41:29', '2022-07-26 20:41:29'),
(6, NULL, NULL, '88888', NULL, '2022-07-26 20:43:52', '2022-07-26 20:43:52'),
(7, NULL, NULL, '123456', NULL, '2022-07-26 22:57:29', '2022-07-26 22:57:29'),
(8, NULL, NULL, '1777777231', NULL, '2022-07-26 23:01:50', '2022-07-26 23:01:50'),
(9, NULL, NULL, '111', NULL, '2022-07-26 23:02:49', '2022-07-26 23:02:49'),
(10, NULL, NULL, '9999', NULL, '2022-07-26 23:08:36', '2022-07-26 23:08:36'),
(11, NULL, NULL, '12356789', NULL, '2022-08-04 17:22:36', '2022-08-04 17:22:36'),
(12, NULL, NULL, '74309273', NULL, '2022-08-04 17:24:12', '2022-08-04 17:24:12'),
(13, NULL, NULL, '8495162', NULL, '2022-08-04 17:27:57', '2022-08-04 17:27:57'),
(14, NULL, NULL, '777444', NULL, '2022-08-04 17:31:02', '2022-08-04 17:31:02');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `actividades_maquina`
--
ALTER TABLE `actividades_maquina`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `actividades_usuario`
--
ALTER TABLE `actividades_usuario`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `maquina`
--
ALTER TABLE `maquina`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `semana_operaciones_maquina`
--
ALTER TABLE `semana_operaciones_maquina`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `session`
--
ALTER TABLE `session`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `actividades_maquina`
--
ALTER TABLE `actividades_maquina`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT de la tabla `actividades_usuario`
--
ALTER TABLE `actividades_usuario`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;

--
-- AUTO_INCREMENT de la tabla `maquina`
--
ALTER TABLE `maquina`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `semana_operaciones_maquina`
--
ALTER TABLE `semana_operaciones_maquina`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `session`
--
ALTER TABLE `session`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
