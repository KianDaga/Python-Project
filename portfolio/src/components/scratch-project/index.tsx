import { Fragment } from 'react';
import { skeleton } from '../../utils';
import LazyImage from '../lazy-image';
import ScratchProjectInterface from '../../interfaces/scratch-project';
import { SanitizedScratch } from '../../interfaces/sanitized-config';

const displaySection = (scratchProjects: ScratchProjectInterface[]) => {
  if (
    scratchProjects &&
    Array.isArray(scratchProjects) &&
    scratchProjects.length
  ) {
    return true;
  } else {
    return false;
  }
};

const ExternalProject = ({
  scratchProjects,
  loading,
  scratchConfig,
}: {
  scratchProjects: ScratchProjectInterface[];
  loading: boolean;
  scratchConfig: SanitizedScratch;
}) => {
  const renderSkeleton = () => {
    const array = [];
    for (let index = 0; index < scratchConfig.limit; index++) {
      array.push(
        <div className="card shadow-lg compact bg-base-100" key={index}>
          <div className="flex justify-between flex-col p-8 h-full w-full">
            <div>
              <div className="flex items-center">
                <span>
                  <h5 className="card-title text-lg">
                    {skeleton({
                      widthCls: 'w-32',
                      heightCls: 'h-8',
                      className: 'mb-1',
                    })}
                  </h5>
                </span>
              </div>
              <div className="mb-5 mt-1">
                {skeleton({
                  widthCls: 'w-full',
                  heightCls: 'h-4',
                  className: 'mb-2',
                })}
                {skeleton({ widthCls: 'w-full', heightCls: 'h-4' })}
              </div>
            </div>
            <div className="flex justify-between">
              <div className="flex flex-grow">
                <span className="mr-3 flex items-center">
                  {skeleton({ widthCls: 'w-12', heightCls: 'h-4' })}
                </span>
                <span className="flex items-center">
                  {skeleton({ widthCls: 'w-12', heightCls: 'h-4' })}
                </span>
              </div>
              <div>
                <span className="flex items-center">
                  {skeleton({ widthCls: 'w-12', heightCls: 'h-4' })}
                </span>
              </div>
            </div>
          </div>
        </div>,
      );
    }

    return array;
  };

  const renderExternalProjects = () => {
    return scratchProjects.map((item, index) => (
      <a
        className="card shadow-lg compact bg-base-100 cursor-pointer"
        key={index}
        href={`https://scratch.mit.edu/projects/${item.id}`}
        onClick={(e) => {
          e.preventDefault();

          window?.open(`https://scratch.mit.edu/projects/${item.id}`, '_blank');
        }}
      >
        <div className="p-8 h-full w-full">
          <div className="flex items-center flex-col">
            <div className="w-full">
              <div className="px-4">
                <div className="text-center w-full">
                  <h2 className="font-semibold text-lg tracking-wide text-center opacity-60 mb-2">
                    {item.title}
                  </h2>
                  {item.image && (
                    <div className="avatar opacity-90">
                      <div className="w-20 h-20 mask mask-squircle">
                        <LazyImage
                          src={item.image}
                          alt={'thumbnail'}
                          placeholder={skeleton({
                            widthCls: 'w-full',
                            heightCls: 'h-full',
                            shape: '',
                          })}
                        />
                      </div>
                    </div>
                  )}
                  <p className="mt-1 text-base-content text-opacity-60 text-sm">
                    {item.instructions}
                  </p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </a>
    ));
  };

  return (
    <Fragment>
      {displaySection(scratchProjects) && (
        <div className="col-span-1 lg:col-span-2">
          <div className="grid grid-cols-2 gap-6">
            <div className="col-span-2">
              <div className="card compact bg-base-100 shadow bg-opacity-40">
                <div className="card-body">
                  <div className="mx-3 flex items-center justify-between mb-2">
                    <h5 className="card-title">
                      {loading ? (
                        skeleton({ widthCls: 'w-40', heightCls: 'h-8' })
                      ) : (
                        <span className="text-base-content opacity-70">
                          My Scratch Projects
                        </span>
                      )}
                    </h5>
                    {loading ? (
                      skeleton({ widthCls: 'w-10', heightCls: 'h-5' })
                    ) : (
                      <a
                        href={`https://scratch.mit.edu/users/${scratchConfig.username}`}
                        target="_blank"
                        rel="noreferrer"
                        className="text-base-content opacity-50 hover:underline"
                      >
                        See All
                      </a>
                    )}
                  </div>
                  <div className="col-span-2">
                    <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                      {loading ? renderSkeleton() : renderExternalProjects()}
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      )}
    </Fragment>
  );
};

export default ExternalProject;
