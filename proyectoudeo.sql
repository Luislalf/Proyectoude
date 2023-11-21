-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 21-11-2023 a las 10:48:12
-- Versión del servidor: 10.4.28-MariaDB
-- Versión de PHP: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `proyectoudeo`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tbl_categorias`
--

CREATE TABLE `tbl_categorias` (
  `categoria_producto` int(11) NOT NULL,
  `nombre_categoria` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `tbl_categorias`
--

INSERT INTO `tbl_categorias` (`categoria_producto`, `nombre_categoria`) VALUES
(1, 'Alimentos'),
(2, 'Higiene y salud');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tbl_clientes`
--

CREATE TABLE `tbl_clientes` (
  `id_cliente` int(11) NOT NULL,
  `nombre_cliente` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `apellido_cliente` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `nit_cliente` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `direccion_cliente` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `tbl_clientes`
--

INSERT INTO `tbl_clientes` (`id_cliente`, `nombre_cliente`, `apellido_cliente`, `nit_cliente`, `direccion_cliente`) VALUES
(1, 'Jose', 'Juarez', '3432335-4', 'Guatemala'),
(3, 'Luis', 'Lopez', '445564-l', 'San Marcos');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tbl_empleados`
--

CREATE TABLE `tbl_empleados` (
  `id_empleado` int(11) NOT NULL,
  `nombre_empleado` varchar(50) DEFAULT NULL,
  `apellido_empleado` varchar(50) DEFAULT NULL,
  `sexo_empleado` int(11) DEFAULT NULL,
  `telefono_empleado` varchar(50) DEFAULT NULL,
  `email_empleado` varchar(50) DEFAULT NULL,
  `profesion_empleado` varchar(50) DEFAULT NULL,
  `foto_empleado` mediumtext DEFAULT NULL,
  `salario_empleado` bigint(20) DEFAULT NULL,
  `fecha_registro` timestamp NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Volcado de datos para la tabla `tbl_empleados`
--

INSERT INTO `tbl_empleados` (`id_empleado`, `nombre_empleado`, `apellido_empleado`, `sexo_empleado`, `telefono_empleado`, `email_empleado`, `profesion_empleado`, `foto_empleado`, `salario_empleado`, `fecha_registro`) VALUES
(5, 'Brenda', 'Viera', 2, '323543543', 'brenda@gmail.com', 'Dev', '22c055aeec314572a0046ec50b84f21719270dac6ea34c91b8380ac289fff9e5.png', 1200000, '2023-08-23 23:05:34'),
(6, 'Alejandro', 'Torres', 1, '324242342', 'alejandro@gmail.com', 'Tecnico', '7b84aceb56534d27aa2e8b727a245dca9f60156a070a47c491ff2d21da1742e5.png', 2100, '2023-08-23 23:06:13'),
(8, 'Arturo', 'Monzon', 1, '3445', 'art@gmail.com', 'Gerente', '70fe91fd94f54a229b90ea0fd800207d1058212885f3468095f0caea90b04583.jpg', 3999, '2023-11-21 01:09:00');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tbl_productos`
--

CREATE TABLE `tbl_productos` (
  `id_producto` int(11) NOT NULL,
  `nombre_producto` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `descripcion_producto` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `cantidad_producto` int(10) DEFAULT NULL,
  `precio_producto` bigint(20) DEFAULT NULL,
  `categoria_producto` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `tbl_productos`
--

INSERT INTO `tbl_productos` (`id_producto`, `nombre_producto`, `descripcion_producto`, `cantidad_producto`, `precio_producto`, `categoria_producto`) VALUES
(1, 'Arroz', 'Libra de arroz', 3, 53, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tbl_proveedores`
--

CREATE TABLE `tbl_proveedores` (
  `id_proveedor` int(11) NOT NULL,
  `nombre_proveedor` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `nit_proveedor` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `direccion_proveedor` varchar(30) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `telefono_proveedor` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `tbl_proveedores`
--

INSERT INTO `tbl_proveedores` (`id_proveedor`, `nombre_proveedor`, `nit_proveedor`, `direccion_proveedor`, `telefono_proveedor`) VALUES
(1, 'Constructora SA', '34323-5', '7MA AVENIDA SAN PEDRO SAC.', '77604523'),
(2, 'IMPRENTA JMM', '34343-4', 'CALLE REAL SAN PEDRO SAC.', '77603322'),
(3, 'AGROPECUARIA MED', '88763-L', 'zona 3 San Marcos', '45673234'),
(5, 'Jazmines', '33435-5', 'Quetzaltenango', '55832467');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `name_surname` varchar(100) NOT NULL,
  `email_user` varchar(50) NOT NULL,
  `pass_user` text NOT NULL,
  `created_user` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `users`
--

INSERT INTO `users` (`id`, `name_surname`, `email_user`, `pass_user`, `created_user`) VALUES
(1, 'Luis1', 'dev@gmail.com', 'scrypt:32768:8:1$SW67AFowPNrAGeyw$6dced9516cc4a7611a7a9bb4c1cb5034044c8ab6d122bd6630e031ce3c18c779984b4c4ddcec10ff5365ebbd10a3535b669c04d592affe8a88cf2acb8b929a19', '2023-07-22 02:10:01'),
(2, 'demo', 'demo@gmail.com', 'scrypt:32768:8:1$Yl2tGU1Ru1Q4Jrzq$d88a0ded538dcfc3a01c8ebf4ea77700576203f6a7cc765f04627464c6047bdcf8eaad84ca3cf0bb5ed058d2dff8ee7a0ba690803538764bedc3ba6173ac6a8a', '2023-07-22 02:29:28');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `tbl_categorias`
--
ALTER TABLE `tbl_categorias`
  ADD PRIMARY KEY (`categoria_producto`);

--
-- Indices de la tabla `tbl_clientes`
--
ALTER TABLE `tbl_clientes`
  ADD PRIMARY KEY (`id_cliente`);

--
-- Indices de la tabla `tbl_empleados`
--
ALTER TABLE `tbl_empleados`
  ADD PRIMARY KEY (`id_empleado`);

--
-- Indices de la tabla `tbl_productos`
--
ALTER TABLE `tbl_productos`
  ADD PRIMARY KEY (`id_producto`),
  ADD KEY `FKCategoria` (`categoria_producto`);

--
-- Indices de la tabla `tbl_proveedores`
--
ALTER TABLE `tbl_proveedores`
  ADD PRIMARY KEY (`id_proveedor`);

--
-- Indices de la tabla `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `tbl_clientes`
--
ALTER TABLE `tbl_clientes`
  MODIFY `id_cliente` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `tbl_empleados`
--
ALTER TABLE `tbl_empleados`
  MODIFY `id_empleado` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT de la tabla `tbl_productos`
--
ALTER TABLE `tbl_productos`
  MODIFY `id_producto` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `tbl_proveedores`
--
ALTER TABLE `tbl_proveedores`
  MODIFY `id_proveedor` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de la tabla `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `tbl_productos`
--
ALTER TABLE `tbl_productos`
  ADD CONSTRAINT `tbl_productos_ibfk_1` FOREIGN KEY (`categoria_producto`) REFERENCES `tbl_categorias` (`categoria_producto`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
