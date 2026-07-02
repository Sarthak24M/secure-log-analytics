import { Card, CardContent, Typography } from "@mui/material";

function SummaryCard({ title, value }) {
    return (
        <Card
            sx={{
                minWidth: 220,
                borderRadius: 3,
                boxShadow: 3
            }}
        >
            <CardContent>

                <Typography
                    color="text.secondary"
                    gutterBottom
                >
                    {title}
                </Typography>

                <Typography
                    variant="h4"
                    fontWeight="bold"
                >
                    {value}
                </Typography>

            </CardContent>
        </Card>
    );
}

export default SummaryCard;