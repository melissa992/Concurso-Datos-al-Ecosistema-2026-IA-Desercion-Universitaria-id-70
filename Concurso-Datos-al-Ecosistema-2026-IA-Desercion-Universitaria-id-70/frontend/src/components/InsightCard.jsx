import React from "react";
import { motion } from "framer-motion";

export default function InsightCard({ title, text }) {
  return (
    <motion.article
      className="insight-card"
      initial={{ opacity: 0, y: 8 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.48 }}
    >
      <h4>{title}</h4>
      <p>{text}</p>
    </motion.article>
  );
}
