import React, { useEffect, useRef } from 'react';
import Chart from 'chart.js/auto';
import DashB from '../../assets/DashIcon.svg';
import Borrowed from '../../assets/TotalBorrowed.svg';
import Returned from '../../assets/TotalReturned.svg';

interface PieChartProps {
  total_borrowed_books: number; // Updated field name
  total_returned_books: number; // Updated field name
}

const PieChart: React.FC<PieChartProps> = ({ total_borrowed_books, total_returned_books }) => {
  const chartRef = useRef<HTMLCanvasElement | null>(null);
  const chartInstanceRef = useRef<Chart | null>(null);

  useEffect(() => {
    if (chartRef.current) {
      if (chartInstanceRef.current) {
        chartInstanceRef.current.destroy();
      }

      const ctx = chartRef.current.getContext('2d');
      if (ctx) {
        chartInstanceRef.current = new Chart(ctx, {
          type: 'pie',
          data: {
            labels: ['Total Borrowed Books', 'Total Returned Books'],
            datasets: [
              {
                data: [total_borrowed_books, total_returned_books],
                backgroundColor: ['#255D81', '#317FB1'],
              },
            ],
          },
          options: {
            responsive: true,
            maintainAspectRatio: true,
            plugins: {
              legend: {
                display: false,
              },
            },
            layout: {
              padding: {
                top: 10,
                bottom: 10,
                left: 10,
                right: 10,
              },
            },
          },
        });
      }
    }

    return () => {
      if (chartInstanceRef.current) {
        chartInstanceRef.current.destroy();
      }
    };
  }, [total_borrowed_books, total_returned_books]);

  return (
    <div className="flex flex-col items-center">
      <canvas ref={chartRef} className="max-w-[300px] max-h-[300px] w-full h-auto" />
      <div className="w-[400px] mt-4 bg-white rounded-md p-4 flex items-center justify-center shadow-md">
        <div className="flex items-center">
          <img src={DashB} alt="Colour Icon" className="w-20 h-20 mr-3" />
          <div>
            <div className="flex items-center">
              <img src={Borrowed} alt="Legend Icon" className="w-5 h-5 mr-1" />
              <span>Total Borrowed Books</span>
            </div>
            <div className="flex items-center">
              <img src={Returned} alt="Legend Icon" className="w-5 h-5 mr-1" />
              <span>Total Returned Books</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default PieChart;