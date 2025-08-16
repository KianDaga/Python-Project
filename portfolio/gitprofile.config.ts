// gitprofile.config.ts

const CONFIG = {
  scratch: {
    username: 'theyoungmaker', //TODO: Your Scratch username. (Required)
    limit: 8, // How many projects to display; maximum 20
    sortBy: 'date', // date | views | remixes
    corsProxy: 'https://scratchapicors-8nbi5t6td-theyoungmaker.vercel.app/', //TODO: Enter your CORS Proxy here
  },
  github: {
    username: 'theyoungmaker', // Your GitHub org/user name. (This is the only required config)
  },
  base: '/gitprofile',
  projects: {
    github: {
      display: true, // Display GitHub projects?
      header: 'Github Projects',
      mode: 'automatic', // Mode can be: 'automatic' or 'manual'
      automatic: {
        sortBy: 'stars', // Sort projects by 'stars' or 'updated'
        limit: 8, // How many projects to display.
        exclude: {
          forks: false, // Forked projects will not be displayed if set to true.
          projects: [], // These projects will not be displayed. example: ['arifszn/my-project1', 'arifszn/my-project2']
        },
      },
      manual: {
        // Properties for manually specifying projects
        // projects: ['arifszn/gitprofile', 'arifszn/pandora'], // List of repository names to display. example: ['arifszn/my-project1', 'arifszn/my-project2']
      },
    },
    external: {
      header: 'My Projects',
      // To hide the `External Projects` section, keep it empty.
      projects: [
        {
          title: 'Microbit Flappy Bird',
          description:
            'This project presents a Flappy Bird-inspired game designed for the Micro:bit v2 platform. It is constructed using for loops, conditional statements, functions, and lists to create an entertaining and interactive gaming experience.',
          imageUrl:
            'https://upload.wikimedia.org/wikipedia/en/0/0a/Flappy_Bird_icon.png',
          link: 'https://makecode.microbit.org/_8hTHCD4ax7ty',
        },
        {
          title: 'Microbit Space Invaders',
          description:
            "This project features a traditional Space Invaders game developed for the Microbit v2 platform. It utilizes while loops, conditional statements, variables, and the Microbit's native game coordinate system to deliver an engaging gaming experience.",
          imageUrl:
            'https://www.svg.com/img/gallery/the-original-idea-behind-space-invaders-that-could-have-changed-gaming-forever/l-intro-1608754172.jpg',
          link: 'https://makecode.microbit.org/_UXqLuYJfJRL6',
        },
      ],
    },
  },
  seo: {
    title: 'Portfolio of The Young Maker',
    description: '',
    imageURL: '',
  },
  social: {
    linkedin: '',
    facebook: '',
    instagram: '',
    tiktok: '',
    email: '',
    website: '',
    twitter: '',
    mastodon: '',
    researchGate: '',
    reddit: '',
    threads: '',
    youtube: '', // example: 'pewdiepie'
    udemy: '',
    dribbble: '',
    behance: '',
    medium: '',
    dev: '',
    stackoverflow: '', // example: '1/jeff-atwood'
    skype: '',
    telegram: '',
    phone: '',
  },
  resume: {
    fileUrl: '', // Empty fileUrl will hide the `Download Resume` button.
  },
  skills: [
    'Scratch',
    'Microbit',
    'JavaScript',
    'Design Thinking',
    'Python',
    'Git',
    'CSS',
    'MakeCode',
    'ScratchJr',
    'Hopscotch',
    'Robotics',
    'Typescript',
  ],
  experiences: [
    {
      company: 'Company Name',
      position: 'Position',
      from: 'September 2021',
      to: 'Present',
      companyLink: 'https://example.com',
    },
    {
      company: 'Company Name',
      position: 'Position',
      from: 'July 2019',
      to: 'August 2021',
      companyLink: 'https://example.com',
    },
  ],
  certifications: [
    {
      name: 'Lorem ipsum',
      body: 'Lorem ipsum dolor sit amet',
      year: 'March 2022',
      link: 'https://example.com',
    },
  ],
  educations: [
    {
      institution: 'Institution Name',
      degree: 'Degree',
      from: '2015',
      to: '2019',
    },
    {
      institution: 'Institution Name',
      degree: 'Degree',
      from: '2012',
      to: '2014',
    },
  ],
  publications: [],
  // Display articles from your medium or dev account. (Optional)
  blog: {
    source: 'dev', // medium | dev
    username: '', // to hide blog section, keep it empty
    limit: 2, // How many articles to display. Max is 10.
  },
  googleAnalytics: {
    id: '', // GA3 tracking id/GA4 tag id UA-XXXXXXXXX-X | G-XXXXXXXXXX
  },
  // Track visitor interaction and behavior. https://www.hotjar.com
  hotjar: {
    id: '',
    snippetVersion: 6,
  },
  themeConfig: {
    defaultTheme: 'lofi',

    // Hides the switch in the navbar
    // Useful if you want to support a single color mode
    disableSwitch: false,

    // Should use the prefers-color-scheme media-query,
    // using user system preferences, instead of the hardcoded defaultTheme
    respectPrefersColorScheme: false,

    // Display the ring in Profile picture
    displayAvatarRing: true,

    // Available themes. To remove any theme, exclude from here.
    themes: [
      'light',
      'dark',
      'cupcake',
      'bumblebee',
      'emerald',
      'corporate',
      'synthwave',
      'retro',
      'cyberpunk',
      'valentine',
      'halloween',
      'garden',
      'forest',
      'aqua',
      'lofi',
      'pastel',
      'fantasy',
      'wireframe',
      'black',
      'luxury',
      'dracula',
      'cmyk',
      'autumn',
      'business',
      'acid',
      'lemonade',
      'night',
      'coffee',
      'winter',
      'dim',
      'nord',
      'sunset',
      'procyon',
    ],

    // Custom theme, applied to `procyon` theme
    customTheme: {
      primary: '#fc055b',
      secondary: '#219aaf',
      accent: '#e8d03a',
      neutral: '#2A2730',
      'base-100': '#E3E3ED',
      '--rounded-box': '3rem',
      '--rounded-btn': '3rem',
    },
  },

  // Optional Footer. Supports plain text or HTML.
  footer: `Made with <a 
  class="text-primary" href="https://github.com/arifszn/gitprofile"
  target="_blank"
  rel="noreferrer"
>GitProfile</a> & <div class="flex items-center"><img src="https://i.ibb.co/L10rd94/TYMLogo-Background.png" width="20" height="20" alt="TYMLogo-Background" border="0" /> <a class="text-primary" href="https://theyoungmaker.com/" target="_blank" rel="noreferrer">The Young Maker </a></div>`,

  enablePWA: true,
};

export default CONFIG;
