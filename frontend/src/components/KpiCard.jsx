import React from "react";
import { motion } from "framer-motion";

export default function KpiCard({
  icon,
  value,
  label,
  delta,
  positive = true,
}) {
  return (
    <motion.div
      className="kpi-card"
      initial={{ opacity: 0, y: 12 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.48 }}
    >
      <div className="kpi-icon">{icon}</div>
      <div className="kpi-body">
        <div className="kpi-value">{value}</div>
        <div className="kpi-label">{label}</div>
      </div>
      <div className={`kpi-delta ${positive ? "positive" : "negative"}`}>
        {delta}
      </div>
    </motion.div>
  );
}
