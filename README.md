# Aadhaar Policy Impact Prediction - Frontend

A modern Next.js frontend for the Aadhaar Policy Impact Prediction System. This application provides an intuitive interface for policy makers to predict and analyze the impact of policy changes on Aadhaar services.

## 🚀 Features

- **Interactive Prediction Interface**: Easy-to-use forms for policy impact analysis
- **Real-time Visualizations**: Charts and graphs showing prediction results
- **Responsive Design**: Works seamlessly on desktop and mobile devices
- **State-wise Analysis**: Detailed breakdown by Indian states
- **Export Capabilities**: Download results in various formats
- **Modern UI**: Built with Tailwind CSS and React components

## 🛠️ Tech Stack

- **Framework**: Next.js 14
- **Language**: TypeScript
- **Styling**: Tailwind CSS
- **Charts**: Chart.js with React Chart.js 2
- **HTTP Client**: Axios
- **Date Handling**: date-fns
- **UI Components**: Custom React components with Lucide icons
- **Deployment**: Vercel

## 📦 Installation

1. Clone the repository:
```bash
git clone https://github.com/ayushkumar2601/uidai_front.git
cd uidai_front
```

2. Install dependencies:
```bash
npm install
```

3. Set up environment variables:
```bash
cp .env.example .env.local
```

Edit `.env.local` and add your backend API URL:
```
NEXT_PUBLIC_API_URL=https://your-backend-api.onrender.com
```

4. Run the development server:
```bash
npm run dev
```

Open [http://localhost:3000](http://localhost:3000) to view the application.

## 🌐 Deployment

### Deploy to Vercel (Recommended)

1. Push your code to GitHub
2. Go to [vercel.com](https://vercel.com) and import your repository
3. Set the environment variable:
   - `NEXT_PUBLIC_API_URL`: Your backend API URL
4. Deploy!

### Manual Deployment

```bash
npm run build
npm run start
```

## 🔧 Configuration

### Environment Variables

- `NEXT_PUBLIC_API_URL`: Backend API URL (required)

### API Integration

The frontend communicates with the Flask backend API. Make sure your backend is deployed and accessible before using the frontend.

Backend endpoints used:
- `GET /health` - Health check
- `GET /api/states` - Get available states
- `POST /api/predict` - Generate predictions

## 📱 Components

### Core Components

- **PredictionForm**: Main form for inputting prediction parameters
- **ResultsDisplay**: Shows prediction results and summaries
- **Charts**: Various chart components for data visualization
- **RegionalImpactTable**: State-wise impact breakdown
- **SummaryCards**: Key metrics display
- **LoadingSpinner**: Loading states
- **RiskAssessment**: Risk level indicators

### Pages

- **Home** (`/`): Main prediction interface
- **API Routes**: Next.js API routes for additional functionality

## 🎨 Styling

The application uses Tailwind CSS for styling with a modern, clean design:

- **Color Scheme**: Blue and gray palette
- **Typography**: Clean, readable fonts
- **Layout**: Responsive grid system
- **Components**: Consistent design system

## 📊 Features in Detail

### Prediction Interface
- Date picker for policy implementation date
- Slider for forecast duration (1-365 days)
- Compliance level adjustment (0-100%)
- State selection (optional)

### Results Visualization
- Summary cards with key metrics
- Daily impact timeline chart
- Regional impact bar chart
- Risk assessment indicators
- Exportable data tables

### Responsive Design
- Mobile-first approach
- Tablet and desktop optimized
- Touch-friendly interface
- Accessible design patterns

## 🔗 Related Repositories

- **Backend API**: [scheme-prediction](https://github.com/ayushkumar2601/scheme-prediction) - Flask API with ML models
- **Documentation**: Comprehensive API and deployment documentation

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆘 Support

If you encounter any issues:

1. Check the [Issues](https://github.com/ayushkumar2601/uidai_front/issues) page
2. Verify your environment variables are set correctly
3. Ensure the backend API is running and accessible
4. Check browser console for error messages

## 🏗️ Architecture

```
User Interface (Next.js/React)
        ↓
API Service Layer (Axios)
        ↓
Backend API (Flask/Render)
        ↓
ML Models & Database
```

## 📈 Performance

- **Lighthouse Score**: 90+ across all metrics
- **Core Web Vitals**: Optimized for performance
- **Bundle Size**: Optimized with Next.js automatic code splitting
- **Caching**: Efficient API response caching

---

Built with ❤️ for better policy decision making