interface Author {
  id: number;
  scratchteam: boolean;
  history: {
    joined: string;
  };
  profile: {
    id: number | null;
    images: {
      '90x90': string;
      '60x60': string;
      '55x55': string;
      '50x50': string;
      '32x32': string;
    };
  };
}

interface Remix {
  parent: number | null;
  root: number | null;
}

interface History {
  created: string;
  modified: string;
  shared: string;
}

interface Stats {
  views: number;
  loves: number;
  favorites: number;
  remixes: number;
}

export default interface ScratchProjectInterface {
  id: number;
  title: string;
  description: string;
  instructions: string;
  visibility: string;
  public: boolean;
  comments_allowed: boolean;
  is_published: boolean;
  author: Author;
  image: string;
  images: {
    '282x218': string;
    '216x163': string;
    '200x200': string;
    '144x108': string;
    '135x102': string;
    '100x80': string;
  };
  history: History;
  stats: Stats;
  remix: Remix;
}
