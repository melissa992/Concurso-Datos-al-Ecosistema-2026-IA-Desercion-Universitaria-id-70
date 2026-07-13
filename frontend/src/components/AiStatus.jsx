import React from "react";
import { motion } from "framer-motion";

export default function AiStatus({ status }) {
  const available = status?.trained ?? false;
  return (
    <motion.div
      className="ai-status"
      initial={{ opacity: 0 }}
      animate={{ opacity: 1 }}
      transition={{ duration: 0.5 }}
    >
      <h3>Estado del Modelo de IA</h3>
      <div className="ai-status-card">
        <div className={`ai-flag ${available ? "available" : "unavailable"}`}>
          {available ? "✔" : "✖"}
        </div>
        <div className="ai-details">
          <div>Modelo: {status?.model || "—"}</div>
          <div>Dataset procesado: {status?.dataset || "—"}</div>
          <div>Variables: {status?.features?.length ?? 0}</div>
          <div>Precisión: {status?.metrics?.accuracy ?? "—"}</div>
          <div>Última ejecución: {status?.last_run ?? "—"}</div>
        </div>
      </div>
    </motion.div>
  );
}
