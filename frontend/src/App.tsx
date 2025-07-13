import { Carousel } from '@mantine/carousel';
import { Image, AspectRatio } from '@mantine/core';

export default function App() {

  const indicators = true
  const loop = true
  const imageUrls = [
    'https://picsum.photos/1920/1080?random=1',
    'https://picsum.photos/1920/1080?random=2',
    'https://picsum.photos/1920/1080?random=3',
    // Add more image URLs here. See https://picsum.photos/ for more information
  ];

  const slides = imageUrls.map((url) => (
    <Carousel.Slide key={url}>
      <Image src={url} />
    </Carousel.Slide>
  ));

  return (
    <AspectRatio ratio={1920 / 1080} >
      <Carousel withIndicators={indicators} loop={loop}>{slides}</Carousel>
    </AspectRatio>
  );
}