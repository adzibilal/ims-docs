'use client';

import Link from 'next/link';
import { motion, Variants } from 'framer-motion';
import { BookOpen, GraduationCap, ChevronRight, LayoutDashboard, ShieldCheck, Zap } from 'lucide-react';

export default function HomePage() {
  const container: Variants = {
    hidden: { opacity: 0 },
    show: {
      opacity: 1,
      transition: {
        staggerChildren: 0.1,
        delayChildren: 0.2,
      },
    },
  };

  const item: Variants = {
    hidden: { opacity: 0, y: 20 },
    show: { opacity: 1, y: 0, transition: { type: 'spring', stiffness: 100, damping: 20 } as any },
  };

  return (
    <div className="relative w-full flex flex-col overflow-hidden bg-zinc-50 dark:bg-zinc-950 selection:bg-emerald-500/30">

      {/* Background Noise & Grain */}
      <div className="pointer-events-none absolute inset-0 z-0 opacity-20 dark:opacity-40 mix-blend-overlay bg-[url('https://grainy-gradients.vercel.app/noise.svg')]" />

      {/* Abstract Glowing Orbs (Desaturated) */}
      <div className="absolute top-[-20%] left-[-10%] w-[50vw] h-[50vw] rounded-full bg-zinc-300/30 dark:bg-emerald-900/10 blur-[120px] pointer-events-none" />
      <div className="absolute bottom-[-10%] right-[-5%] w-[40vw] h-[40vw] rounded-full bg-zinc-200/40 dark:bg-zinc-800/30 blur-[100px] pointer-events-none" />

      {/* Main Content Area */}
      <main className="relative z-10 flex-1 flex items-center justify-center max-w-[1400px] mx-auto px-6 py-20 lg:py-32 w-full">
        <div className="grid grid-cols-1 lg:grid-cols-12 gap-16 lg:gap-8 w-full items-center">

          {/* Left Column: Asymmetric Typography */}
          <motion.div
            className="lg:col-span-7 flex flex-col items-start text-left"
            variants={container}
            initial="hidden"
            animate="show"
          >
            <motion.div variants={item} className="inline-flex items-center gap-2 px-3 py-1.5 rounded-full bg-zinc-200/50 dark:bg-white/5 border border-zinc-300/50 dark:border-white/10 mb-8 backdrop-blur-md">
              <span className="flex h-2 w-2 rounded-full bg-emerald-500 animate-pulse" />
              <span className="text-sm font-medium text-zinc-700 dark:text-zinc-300 tracking-wide">Sistem Dokumentasi</span>
            </motion.div>

            <motion.h1
              variants={item}
              className="text-5xl sm:text-6xl lg:text-7xl font-bold tracking-tighter leading-[1.05] text-zinc-900 dark:text-zinc-50 mb-6"
            >
              Arsitektur <br className="hidden sm:block" />
              <span className="text-transparent bg-clip-text bg-linear-to-r from-zinc-700 to-zinc-400 dark:from-zinc-100 dark:to-zinc-500">
                Pendidikan Modern.
              </span>
            </motion.h1>

            <motion.p
              variants={item}
              className="text-lg sm:text-xl text-zinc-600 dark:text-zinc-400 max-w-[55ch] leading-relaxed mb-10"
            >
              Pusat referensi dan panduan operasional IMS Dashboard. Dirancang untuk memberikan transparansi penuh bagi Administrator dan Tenaga Pengajar dalam mengelola siklus akademik.
            </motion.p>

            <motion.div variants={item} className="flex flex-col sm:flex-row gap-4 w-full sm:w-auto">
              <Link
                href="/docs/admin"
                className="group relative flex items-center justify-center gap-2 px-8 py-4 bg-zinc-900 dark:bg-zinc-100 text-zinc-50 dark:text-zinc-900 rounded-xl font-semibold overflow-hidden transition-all hover:scale-[0.98] active:scale-95 shadow-xl shadow-zinc-900/10 dark:shadow-zinc-100/10"
              >
                <ShieldCheck className="w-5 h-5" />
                <span>Panduan Administrator</span>
                <ChevronRight className="w-4 h-4 group-hover:translate-x-1 transition-transform" />
              </Link>

              <Link
                href="/docs/teacher"
                className="group flex items-center justify-center gap-2 px-8 py-4 bg-transparent border border-zinc-300 dark:border-zinc-800 text-zinc-800 dark:text-zinc-200 hover:bg-zinc-100 dark:hover:bg-white/5 rounded-xl font-semibold transition-all hover:scale-[0.98] active:scale-95"
              >
                <GraduationCap className="w-5 h-5" />
                <span>Panduan Guru</span>
              </Link>
            </motion.div>
          </motion.div>

          {/* Right Column: Liquid Glass Interactive Cards */}
          <motion.div
            className="lg:col-span-5 relative mt-8 lg:mt-0"
            variants={container}
            initial="hidden"
            animate="show"
          >
            {/* Main Glass Card */}
            <motion.div
              variants={item}
              className="relative z-20 w-full p-8 rounded-3xl bg-white/40 dark:bg-zinc-900/40 backdrop-blur-xl border border-white/60 dark:border-white/10 shadow-[0_8px_32px_rgba(0,0,0,0.04)] dark:shadow-[inset_0_1px_0_rgba(255,255,255,0.05)] overflow-hidden"
            >
              <div className="flex items-center gap-4 mb-8">
                <div className="p-3 bg-emerald-500/10 text-emerald-600 dark:text-emerald-400 rounded-xl">
                  <LayoutDashboard className="w-6 h-6" />
                </div>
                <div>
                  <h3 className="font-semibold text-zinc-900 dark:text-zinc-100">Cepat & Responsif</h3>
                  <p className="text-sm text-zinc-500 dark:text-zinc-400">Navigasi tanpa hambatan.</p>
                </div>
              </div>

              <div className="space-y-4">
                {[
                  { title: 'Manajemen Kelas', desc: 'Atur jadwal & sesi mudah' },
                  { title: 'Siklus Payroll', desc: 'Hitung gaji secara otomatis' },
                  { title: 'Absensi Siswa', desc: 'Rekap kehadiran real-time' },
                ].map((feature, idx) => (
                  <div key={idx} className="flex items-center justify-between p-4 rounded-xl bg-white/60 dark:bg-zinc-800/50 border border-transparent dark:border-white/5 hover:border-zinc-300 dark:hover:border-white/10 transition-colors">
                    <div className="flex items-center gap-3">
                      <Zap className="w-4 h-4 text-zinc-400" />
                      <span className="font-medium text-zinc-700 dark:text-zinc-300">{feature.title}</span>
                    </div>
                    <span className="text-xs text-zinc-400 dark:text-zinc-500">{feature.desc}</span>
                  </div>
                ))}
              </div>
            </motion.div>

            {/* Decorative Floating Element Behind */}
            <motion.div
              variants={item}
              animate={{ y: [0, -10, 0] }}
              transition={{ repeat: Infinity, duration: 5, ease: "easeInOut" }}
              className="absolute -bottom-[45%] -right-8 z-[99] p-6 rounded-2xl bg-zinc-900 dark:bg-zinc-800 border border-zinc-800 dark:border-zinc-700 shadow-2xl hidden sm:block"
            >
              <div className="flex items-center gap-4">
                <motion.div variants={item} className="">
                  <img src="/ims-landscape.png" alt="IMS Logo" className="h-30 w-auto drop-shadow-xl dark:hidden" />
                  <img src="/ims-landscape.png" alt="IMS Logo" className="h-30 w-auto drop-shadow-xl hidden dark:block" />
                </motion.div>
              </div>
            </motion.div>
          </motion.div>

        </div>
      </main>
    </div>
  );
}
