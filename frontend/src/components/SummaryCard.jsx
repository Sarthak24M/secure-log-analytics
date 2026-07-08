import { Card, CardContent, Typography, Box } from "@mui/material";

function SummaryCard({ title, value, icon, accentColor, onClick }) {
    return (
        <Card
            onClick={onClick}
            sx={{
                minWidth: 200,
                flex: "1 1 180px",
                cursor: onClick ? "pointer" : "default",
                borderTop: `3px solid ${accentColor || "#00bcd4"}`,
                "&:hover": onClick
                    ? { transform: "translateY(-3px)" }
                    : {},
            }}
        >
            <CardContent sx={{ p: 3 }}>
                <Box sx={{ display: "flex", justifyContent: "space-between", alignItems: "flex-start" }}>
                    <Typography
                        variant="body2"
                        sx={{ color: "text.secondary", mb: 1.5, fontSize: "0.78rem", textTransform: "uppercase", letterSpacing: "0.06em" }}
                    >
                        {title}
                    </Typography>
                    {icon && (
                        <Box sx={{ color: accentColor || "primary.main", opacity: 0.8 }}>
                            {icon}
                        </Box>
                    )}
                </Box>
                <Typography variant="h4" fontWeight={700} sx={{ color: "text.primary" }}>
                    {value ?? "—"}
                </Typography>
                {onClick && (
                    <Typography variant="caption" sx={{ color: "text.secondary", mt: 1, display: "block" }}>
                        Click to view logs
                    </Typography>
                )}
            </CardContent>
        </Card>
    );
}

export default SummaryCard;