
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
(471, 1, 10, '2022-08-29 15:56:36', '2022-08-29 15:56:36');

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
(480, 2, 0, 0, 0, 0, 0, 0, '2022-08-29 15:56:36', '2022-08-29 15:56:36', 1);

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
(412, 16, '2022-08-29 15:56:49', '2022-08-29 15:56:49', '2022-08-29 15:56:49');

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
  `updated_at` timestamp NULL DEFAULT current_timestamp(),
  `cargo` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `usuarios`
--

INSERT INTO `usuarios` (`id`, `nombre`, `password`, `dni`, `isAdmin`, `created_at`, `updated_at`, `cargo`) VALUES
(1, 'cristian', '123456', '74309887', 1, '2022-07-26 14:52:17', '2022-07-26 14:52:17', 'OPERARIO'),
(2, 'Mantenimiento', '123456', '7456123', 1, '2022-07-26 15:16:39', '2022-07-26 15:16:39', 'MANTENIMIENTO'),
(16, 'operario', '123456', NULL, NULL, '2022-08-24 23:12:33', '2022-08-24 23:12:33', 'OPERARIO'),
(17, 'logistica', '123456', NULL, NULL, '2022-08-24 23:12:33', '2022-08-24 23:12:33', 'LOGISTICA'),
(18, 'RRHH', '123456', NULL, NULL, '2022-08-24 23:12:58', '2022-08-24 23:12:58', 'RECURSOSHUMANOS');

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
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=472;

--
-- AUTO_INCREMENT de la tabla `actividades_usuario`
--
ALTER TABLE `actividades_usuario`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=481;

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
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=413;

--
-- AUTO_INCREMENT de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;
COMMIT;
