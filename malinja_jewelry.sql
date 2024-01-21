-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 17, 2024 at 04:07 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `malinja_jewelry`
--

-- --------------------------------------------------------

--
-- Table structure for table `customer_information`
--

CREATE TABLE `customer_information` (
  `customer_name` text NOT NULL,
  `customer_age` int(3) NOT NULL,
  `title` varchar(10) NOT NULL,
  `customer_address` varchar(300) NOT NULL,
  `customer_phone` varchar(12) NOT NULL,
  `customer_email` varchar(50) NOT NULL,
  `customer_gender` text NOT NULL,
  `customer_nationality` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Dumping data for table `customer_information`
--

INSERT INTO `customer_information` (`customer_name`, `customer_age`, `title`, `customer_address`, `customer_phone`, `customer_email`, `customer_gender`, `customer_nationality`) VALUES
('MUHAMMAD HANIF AIMAN BIN KAMARUZAMAN ', 23, 'Mr.', 'kolej malinja', '01121955708', 'hanifaiman2004@gmail.com', 'Male', 'Malay'),
('danish', 0, 'Datin', '5u3', 'wrgewtjie7', '4i4', 'Male', 'Malay'),
('hakim', 56, 'Dato', '', '01265483235', '', 'Male', ''),
('', 0, '', '', '', '', '', ''),
('MUHAMMAD AMMAR ', 21, 'Dato', 'kampung sungai petani', '0149306123', 'ammar@gmail.com', 'Male', 'Malay'),
('IZZAT ALI ', 24, 'Dato', 'jalan 15, taman permai', '0124356786', 'ALI@gmail.com', 'Male', 'Indian'),
('Johan iskandar', 33, 'Mr.', '', '0147864675', 'jo@gmail.com', 'Male', 'Malay'),
('HANIF AIMAN KAMARUZAMAN', 56, 'Dr.', 'taman hulu terengganu', '0123456758', 'aiman@gmail.com', 'Male', 'Iban'),
('fakhrul mirza', 21, 'Mr.', '', '0198776745', 'mirza@gmail.com', 'Male', 'Kadazan'),
('lee jung kuk', 53, 'Tan Sri', 'taman permai indah', '0124553678', 'izzudin@gmail.com', 'Male', 'Chinese'),
('muhammad rajesh', 32, 'Mr.', 'jalan jaya diri', '0173425667', 'rajesh@gmail.com', 'Male', 'Indian'),
('nurul aisyah', 32, 'Datin', 'taman megah indah ', '0167846752', 'aisyah@gmail.com', 'Female', 'Malay'),
('', 0, '', '', '', '', '', ''),
('wawa lavender', 23, 'Mrs.', 'puchong,selangor', '0117895432', 'waw342@gmail.com', 'Female', 'Chinese'),
('Johan Putra Shazlan', 25, 'Dato', 'London', '0184006135', 'joputralan@gmail.com', 'Female', 'Iban'),
('alfira zubaidah', 19, 'Mrs.', 'sabah', '0178554321', 'alfira02@gmail.com', 'Female', 'Kadazan'),
('irfan haqeem', 30, 'Dr.', 'petaling jaya, selangor', '0125667890', 'irfanhaq@gmail.com', 'Male', 'Malay');

-- --------------------------------------------------------

--
-- Table structure for table `order_jewelry`
--

CREATE TABLE `order_jewelry` (
  `item_value` varchar(200) NOT NULL,
  `product_value` varchar(200) NOT NULL,
  `quantity_value` varchar(200) NOT NULL,
  `total_price` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Dumping data for table `order_jewelry`
--

INSERT INTO `order_jewelry` (`item_value`, `product_value`, `quantity_value`, `total_price`) VALUES
(' fish bracelets', '350', '4', '1400'),
('meteor bracelets', '600', '4', '2400'),
('flower bracelets', '1190', '4', '4760'),
('dino necklace', '4093', '5', '20465'),
('flower bracelets', '600', '3', '1800'),
('diamond ring', '10023', '7', '70161'),
('cat necklace', '7183', '9', '64647'),
('shark necklace', '6086', '27', '164322'),
('flower bracelets', '1190', '3', '3570'),
('cat necklace', '7183', '4', '28732'),
('flower bracelets', '1190', '2', '2380'),
('diamond ring', '10023', '2', '20046'),
(' fish bracelets', '350', '2', '700'),
('silver ring', '1297', '1', '1297');

-- --------------------------------------------------------

--
-- Table structure for table `order_tracking`
--

CREATE TABLE `order_tracking` (
  `free_gift` varchar(200) NOT NULL,
  `claim_place` varchar(200) NOT NULL,
  `claim_date` date NOT NULL,
  `additional_notes` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Dumping data for table `order_tracking`
--

INSERT INTO `order_tracking` (`free_gift`, `claim_place`, `claim_date`, `additional_notes`) VALUES
('Perfume', 'Hulu Teregganu,Terengganu (014-9307134)', '0000-00-00', 'give me a nice quality'),
('Beg', 'Batu Pahat,Johor(014-7726817)', '2024-01-31', 'hope have nice quality'),
('', '', '2024-01-17', ''),
('Umbrella', 'Hulu Teregganu,Terengganu (014-9307134)', '2024-01-17', 'thank you'),
('Beg', 'Petaling Jaya,Selangor (014-8726615)', '2024-01-17', 'terima kasih'),
('Beg', 'Hulu Teregganu,Terengganu (014-9307134)', '2024-01-17', 'buat cantik cantik ya'),
('Perfume', 'Petaling Jaya,Selangor (014-8726615)', '2024-01-17', 'okayyy'),
('Beg', 'Alor Gajah, Melaka (014-3528817)) ', '2024-01-17', 'thank youu'),
('Perfume', 'Petaling Jaya,Selangor (014-8726615)', '2024-01-31', '-'),
('Umbrella', 'Alor Gajah, Melaka (014-3528817)) ', '2024-01-22', 'terima kasihh'),
('Perfume', 'Petaling Jaya,Selangor (014-8726615)', '2024-01-31', 'datang padpkul 3.00pm'),
('Perfume', 'Petaling Jaya,Selangor (014-8726615)', '2024-01-18', 'arigatou'),
('Beg', 'Batu Pahat,Johor(014-7726817)', '2024-01-25', 'package it nicely okay!!'),
('Beg', 'Hulu Teregganu,Terengganu (014-9307134)', '2024-01-19', 'thank you for buying from us');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
